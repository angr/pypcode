#!/usr/bin/env python
import argparse
import logging
import os
import os.path
import sys
from difflib import SequenceMatcher

from pypcode import *

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='[%(name)s:%(levelname)s] %(message)s')

def main():
  ap = argparse.ArgumentParser(prog='pypcode', description='Disassemble and translate machine code to P-code using SLEIGH')
  ap.add_argument('-l', '--list', action='store_true', help='list architecture languages')
  ap.add_argument('langid', help='architecture language id')
  ap.add_argument('binary', help='path to flat binary code')
  ap.add_argument('base', default='0', nargs='?', help='base address to load at')
  ap.add_argument('-o', '--offset', default='0', help='offset in binary file to load from')
  ap.add_argument('-s', '--length', default=None, help='length of code in bytes to load')
  ap.add_argument('-i', '--max-instructions', default=0, type=int, help='maximum number of instructions to translate')

  langs = {}
  for arch in Arch.enumerate():
    for lang in arch.languages:
      langs[lang.id] = lang

  # List supported languages
  if ('-l' in sys.argv) or ('--list' in sys.argv):
    for langid in sorted(langs):
      print('%-35s - %s' % (langid, langs[langid].description))
    return

  args = ap.parse_args()

  # Get requested language
  if args.langid not in langs:
    print(f'Language "{args.langid}" not found.')
    t = args.langid.upper()
    suggestions = [l for l in langs if SequenceMatcher(None, t, l.split()[0].upper()).ratio() > 0.25]
    if len(suggestions):
      print('\nSuggestions:')
      for langid in sorted(suggestions):
        print('  %-35s - %s' % (langid, langs[langid].description))
      print('')
    print('Try `--list` for full list of architectures.')
    return
  lang = langs[args.langid]

  # Load target binary code
  base = int(args.base, 0)
  with open(args.binary, 'rb') as f:
    f.seek(int(args.offset, 0))
    code = bytearray(f.read(int(args.length, 0)) if args.length else f.read())

  # Init SLEIGH
  log.debug('Loading image')
  loader = SimpleLoadImage(base, code, len(code))
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
  trans.initialize(docstorage)
  log.debug('Initializing context')
  lang.init_context_from_pspec(context)

  # Translate
  emit     = PcodeRawOutHelper(trans)
  asm      = AssemblyEmitCacher()
  addr     = Address(trans.getDefaultCodeSpace(), base)
  lastaddr = Address(trans.getDefaultCodeSpace(), base + len(code))

  def vardata_str(data):
    s = '(%s, 0x%x, %d) ' % (data.space.getName(), data.offset, data.size)
    if data.space.getName() == 'register':
      regname = trans.getRegisterName(data.space, data.offset, data.size)
      s += '{%s} ' % regname
    return s

  num_insn_xlat = 0
  while (addr.getOffset() < lastaddr.getOffset()
    and (args.max_instructions == 0 or num_insn_xlat < args.max_instructions)):
    try:
      emit.clearCache()
      trans.printAssembly(asm, addr)
      length = trans.oneInstruction(emit, addr)
      print('%08x/%d: %s %s' % (asm.addr.getOffset(), length, asm.mnem, asm.body))
      for op in emit.opcache:
        out  = op.getOutput()
        outs = (vardata_str(out) + '=') if out else ''
        var  = ' '.join(vardata_str(op.getInput(i)) for i in range(op.numInput()))
        print('%-30s %-12s %s' % (outs, get_opname(op.getOpcode()), var))
      print('')
      addr = addr + length

    except Exception as e:
      print(e)
      break

    num_insn_xlat += 1

if __name__ == '__main__':
	main()
