#!/usr/bin/env python
import sys
from pypcode import *

def main():
  
  if len(sys.argv) != 2:
    sys.stderr.write("USAGE:  " + sys.argv[0] + " disassemble\n")
    sys.stderr.write("        " + sys.argv[0] + " pcode\n")
    sys.stderr.write("        " + sys.argv[0] + " emulate\n")
    sys.exit(2);
  action = sys.argv[1]

  log.debug('Loading image')
  loader = cppyy.gbl.MyLoadImage(0x80483b4, myprog, len(myprog))

  # Set up the context object
  log.debug('Creating context')
  context = cppyy.gbl.ContextInternal()

  # Set up the assembler/pcode-translator
  log.debug('Setting up translator')
  sleighfilename = os.path.join(SLEIGH_SPECFILES_PATH, 'x86.sla')
  trans = cppyy.gbl.Sleigh(loader, context)

  log.debug('Reading Sleigh file into DOM')
  docstorage = cppyy.gbl.DocumentStorage()

  log.debug('Opening document')
  doc = docstorage.openDocument(sleighfilename).getRoot()

  log.debug('Registering tags')
  docstorage.registerTag(doc)
  
  log.debug('Initializing translator')
  trans.initialize(docstorage) # Initialize the translator
  log.debug('Ok')

  # Now that context symbol names are loaded by the translator
  # we can set the default context
  context.setVariableDefault("addrsize",1) # Address size is 32-bit
  context.setVariableDefault("opsize",1) # Operand size is 32-bit
  
  if action == "disassemble":
    dumpAssembly(trans);
  elif action == "pcode":
    dumpPcode(trans)
  elif action == "emulate":
    cppyy.gbl.doEmulation(trans, loader)
  else:
    sys.stdout.write("Unknown action: " + action + "\n")

if __name__ == '__main__':
	main()
