pypcode ![Build Status](https://github.com/angr/pypcode/workflows/Build/badge.svg?event=push)
=======
Experimental Python bindings to Ghidra's [SLEIGH](https://ghidra.re/courses/languages/html/sleigh.html) library. Currently building for Linux-based systems, though cross-platform support is not far away (PRs welcome).

Install
-------
Install with PIP and Git via:

```bash
python3 -m pip install --user git+https://github.com/angr/pypcode
```

Example Usage
-------------
See `__main__.py` for example usage which converts a chunk of x86 code to pcode.

License
-------
SLEIGH is licensed under Apache 2. Please see full license details and disclaimers in this repo at docs/ghidra/LICENSE.
