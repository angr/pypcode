#!/usr/bin/env python
import sys
import logging
from pypcode import *
import argparse
import os
import os.path
from difflib import SequenceMatcher
import xml.etree.ElementTree as ET

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='[%(name)s:%(levelname)s] %(message)s')

class Arch:
  def __init__(self, archname, ldefpath):
    self.archpath = os.path.dirname(ldefpath)
    self.archname = archname
    self.ldefpath = ldefpath
    self.ldef = ET.parse(ldefpath)
    self.langs = [ArchLanguage(self.archpath, e) for e in self.ldef.getroot()]

  @classmethod
  def enumerate(cls):
    # processors/<architecture>/data/languages/<variant>.ldef
    for archname in os.listdir(SLEIGH_SPECFILES_PATH):
      langdir = os.path.join(SLEIGH_SPECFILES_PATH, archname, 'data', 'languages')
      if not (os.path.exists(langdir) and os.path.isdir(langdir)): continue
      for langname in os.listdir(langdir):
        if not langname.endswith('.ldefs'): continue
        ldefpath = os.path.join(langdir, langname)
        yield Arch(archname, ldefpath)

class ArchLanguage:
  def __init__(self, archdir, ldef):
    self.archdir = archdir
    self.ldef = ldef

  @property
  def pspec_path(self):
    return os.path.join(self.archdir, self.processorspec)

  @property
  def slafile_path(self):
    return os.path.join(self.archdir, self.slafile)

  @property
  def description(self):
    return self.ldef.find('description').text

  def __getattr__(self, key):
    if key in self.ldef.attrib:
      return self.ldef.attrib[key]
    super().__attr__(key)

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument('-l', '--list', action='store_true', help='list architecture languages')
  ap.add_argument('lang', help='architecture language')
  ap.add_argument('binary', help='path to flat binary code')
  ap.add_argument('base', default='0', nargs='?', help='base address in hex')

  langs = {}
  for arch in Arch.enumerate():
    for lang in arch.langs:
      langs[lang.id] = lang

  if ('-l' in sys.argv) or ('--list' in sys.argv):
    for langid in sorted(langs):
      print('%-35s - %s' % (langid, langs[langid].description))
    return

  args = ap.parse_args()

  if args.lang not in langs:
    print(f'Language "{args.lang}" not found.')
    suggestions = [l for l in langs if SequenceMatcher(None, args.lang.upper(), l.split()[0].upper()).ratio() > 0.25]
    if len(suggestions):
      print('\nSuggestions:')
      for langid in sorted(suggestions):
        print('  %-35s - %s' % (langid, langs[langid].description))
      print('')
    print('Try `--list` for full list of architectures.')
    return

  lang = langs[args.lang]

  code = bytearray(open(args.binary, 'rb').read())
  start = int(args.base, 16)

  log.debug('Loading image')
  loader = SimpleLoadImage(start, code, len(code))

  log.debug('Creating context')
  context = ContextInternal()

  log.debug('Setting up translator')
  trans = Sleigh(loader, context)

  log.debug('Reading Sleigh file into DOM')
  docstorage = DocumentStorage()

  log.debug('Opening document')
  doc = docstorage.openDocument(lang.slafile_path).getRoot()

  log.debug('Registering tags')
  docstorage.registerTag(doc)

  log.debug('Initializing translator')
  trans.initialize(docstorage) # Initialize the translator

  log.debug('Initializing context')
  pspec = ET.parse(lang.pspec_path)
  cd = pspec.getroot().find('context_data')
  if cd:
    cs = cd.find('context_set')
    if cs:
      for e in cs:
        assert(e.tag == 'set')
        context.setVariableDefault(e.attrib['name'], int(e.attrib['val']))

  emit = PcodeRawOutHelper(trans) # Set up the pcode dumper
  asm = AssemblyEmitCacher() # Set up the disassembly dumper
  addr = Address(trans.getDefaultCodeSpace(), start) # First address to translate
  lastaddr = Address(trans.getDefaultCodeSpace(), start+len(code)) # Last address

  def print_vardata(data):
    sys.stdout.write('(%s, 0x%x, %d) ' % (data.space.getName(), data.offset, data.size))
    if data.space.getName() == 'register':
      regname = trans.getRegisterName(data.space, data.offset, data.size)
      sys.stdout.write('{%s} ' % regname)

  while addr.getOffset() < lastaddr.getOffset():
    try:
      emit.clearCache()

      # Disassemble this instruction
      trans.printAssembly(asm, addr)
      print('%08x: %s %s' % (asm.addr.getOffset(), asm.mnem, asm.body))

      # Translate instruction to P-code
      length = trans.oneInstruction(emit, addr)
      for op in emit.opcache:
        out = op.getOutput()
        if out:
          print_vardata(out)
          sys.stdout.write('= ')
        sys.stdout.write('%s ' % get_opname(op.getOpcode()))
        for i in range(op.numInput()):
          print_vardata(op.getInput(i))
        sys.stdout.write('\n')

      sys.stdout.write('\n')
      addr = addr + length # Advance to next instruction

    except Exception as e:
      print(e)
      break

if __name__ == '__main__':
	main()
