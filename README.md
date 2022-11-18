pypcode
=======
[![pypi](https://img.shields.io/pypi/v/pypcode)](https://pypi.org/project/pypcode/)

Machine code disassembly and IR translation library for Python using the
excellent [SLEIGH](https://ghidra.re/courses/languages/html/sleigh.html)
library from the [Ghidra](https://ghidra-sre.org/) framework (version 10.2.2).

This library was created primarily for use with [angr](http://angr.io), which
provides analyses and symbolic execution of p-code.

Quick Start
-----------
This package can be installed on Linux, macOS, and Windows platforms for recent
(3.8+) versions of both CPython and PyPy. Wheels are provided for several
configurations. You can install the latest release from PyPI using `pip`:

```bash
pip install pypcode
```

You can also install the very latest development version from this repository
using `pip`:

```bash
pip install --user https://github.com/angr/pypcode/archive/refs/heads/master.zip
```

You can now invoke the `pypcode` module from command line to translate supported
machine code to P-code from command line. Run `python -m pypcode --help` for
usage information. See module source (`__main__.py`) for examples of using
pypcode as a library.

Example
-------

```
$ python -m pypcode -b x86:LE:64:default test-x64.bin
--------------------------------------------------------------------------------
00000000/2: XOR EAX,EAX
--------------------------------------------------------------------------------
  0: CF = 0x0
  1: OF = 0x0
  2: EAX = EAX ^ EAX
  3: RAX = zext(EAX)
  4: SF = EAX s< 0x0
  5: ZF = EAX == 0x0
  6: unique[0x2580:4] = EAX & 0xff
  7: unique[0x2590:1] = popcount(unique[0x2580:4])
  8: unique[0x25a0:1] = unique[0x2590:1] & 0x1
  9: PF = unique[0x25a0:1] == 0x0

--------------------------------------------------------------------------------
00000002/2: CMP ESI,EAX
--------------------------------------------------------------------------------
  0: CF = ESI < EAX
  1: OF = sborrow(ESI, EAX)
  2: unique[0x5180:4] = ESI - EAX
  3: SF = unique[0x5180:4] s< 0x0
  4: ZF = unique[0x5180:4] == 0x0
  5: unique[0x2580:4] = unique[0x5180:4] & 0xff
  6: unique[0x2590:1] = popcount(unique[0x2580:4])
  7: unique[0x25a0:1] = unique[0x2590:1] & 0x1
  8: PF = unique[0x25a0:1] == 0x0

--------------------------------------------------------------------------------
00000004/2: JBE 0x17
--------------------------------------------------------------------------------
  0: unique[0x18f0:1] = CF || ZF
  1: if (unique[0x18f0:1]) goto ram[0x17:8]
```
