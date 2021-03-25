pypcode ![Build Status](https://github.com/angr/pypcode/workflows/Build/badge.svg?event=push)
=======
Machine code disassembly and IR translation library for Python using the
excellent [SLEIGH](https://ghidra.re/courses/languages/html/sleigh.html) library
from the [Ghidra](https://ghidra-sre.org/) framework. Primarily for use in
[angr](http://angr.io).

Quick Start
-----------
This package can be installed on Linux, macOS, and Windows platforms for recent
versions of both CPython and PyPy. You will need a working compiler and CMake to
build the bindings.

Install with PIP+Git via:

```bash
python3 -m pip install --user git+https://github.com/angr/pypcode
```

You can now invoke the `pypcode` module from command line to translate supported
machine code to P-code from command line. Run `python -m pypcode --help` for
usage information. See module source for examples of using pypcode as a library.
