#!/usr/bin/env python
"""
Runs when invoking pypcode module from command line. Lists supported
architectures, and handles basic disassembly and translation to P-code of
supported binaries. Does not parse object files, the binary files must be plain
machine code bytes in a file.
"""

import argparse
import logging
import sys
from difflib import SequenceMatcher

from pypcode import Arch, Context, PcodePrettyPrinter

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='[%(name)s:%(levelname)s] %(message)s')


def main():
  ap = argparse.ArgumentParser(prog='pypcode', description='Disassemble and translate machine code to P-code using SLEIGH')
  ap.add_argument('-l', '--list', action='store_true', help='list supported architecture languages')
  ap.add_argument('langid', help='architecture language id')
  ap.add_argument('binary', help='path to flat binary code')
  ap.add_argument('base', default='0', nargs='?', help='base address to load at')
  ap.add_argument('-o', '--offset', default='0', help='offset in binary file to load from')
  ap.add_argument('-s', '--length', default=None, help='length of code in bytes to load')
  ap.add_argument('-i', '--max-instructions', default=0, type=int, help='maximum number of instructions to translate')
  ap.add_argument('-r', '--raw', action='store_true', default=False, help='show raw p-code (disable pretty-printing)')
  ap.add_argument('-b', '--basic-block', action='store_true', default=False, help='stop translation at end of basic block')

  # List supported languages
  langs = {l.id:l for arch in Arch.enumerate() for l in arch.languages}
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
    exit(1)

  # Load target binary code
  base = int(args.base, 0)
  with open(args.binary, 'rb') as f:
    f.seek(int(args.offset, 0))
    code = f.read(int(args.length, 0)) if args.length else f.read()

  # Translate
  ctx = Context(langs[args.langid])
  res = ctx.translate(code, base, args.max_instructions, bb_terminating=args.basic_block)

  for insn in res.instructions:
    print('-' * 80)
    print('%08x/%d: %s %s' % (insn.address.offset, insn.length, insn.asm_mnem, insn.asm_body))
    print('-' * 80)
    for op in insn.ops:
      print('%3d: %s' % (op.seq.uniq, str(op) if args.raw else PcodePrettyPrinter.fmt_op(op)))
    print('')

  if res.error:
    print('** An error occured during translation: ' + repr(res.error))

if __name__ == '__main__':
	main()
