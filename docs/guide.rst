Guide
=====

Installation
------------
This package can be installed on Linux, macOS, and Windows platforms for recent (3.8+) versions of both CPython and
PyPy. Wheels are provided for several configurations. The latest release can be installed from PyPI using ``pip``:

.. code:: bash

   pip install pypcode

The very latest development version can be installed from GitHub via:

.. code:: bash

   pip install --user https://github.com/angr/pypcode/archive/refs/heads/master.zip

Usage Example
-------------

Disassemble with :meth:`pypcode.Context.disassemble`:

.. ipython::

   In [0]: from pypcode import Context
      ...: ctx = Context("x86:LE:64:default")
      ...: dx = ctx.disassemble(bytes.fromhex("483578563412c3"))
      ...: print(dx)

Work with :class:`pypcode.Disassembly` and :class:`pypcode.Instruction`:

.. ipython::

   In [0]: (dx.instructions[0].mnem, dx.instructions[0].body)

Translate to P-Code with :meth:`pypcode.Context.translate`:

.. ipython::

   In [0]: from pypcode import Context
      ...: ctx = Context("x86:LE:64:default")
      ...: tx = ctx.translate(bytes.fromhex("483578563412c3"))
      ...: print(tx)

Work with :class:`pypcode.Translation` and :class:`pypcode.PcodeOp`:

.. ipython::

   In [0]: tx.ops[3].opcode

   In [0]: tx.ops[3].inputs[0].space.name

   In [0]: tx.ops[3].inputs[0].getRegisterName()


Command Line Usage Example
--------------------------
The ``pypcode`` module can be invoked from command line to disassemble and translate supported machine code to P-code
from command line. Run ``python -m pypcode --help`` for usage information.

::

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

SLEIGH & P-Code References
--------------------------
Extensive documentation covering SLEIGH and P-Code is available online:

* `SLEIGH, P-Code Introduction <https://htmlpreview.github.io/?https://github.com/NationalSecurityAgency/ghidra/blob/Ghidra_11.4.1_build/GhidraDocs/languages/html/sleigh.html>`_
* `P-Code Reference Manual <https://htmlpreview.github.io/?https://github.com/NationalSecurityAgency/ghidra/blob/Ghidra_11.4.1_build/GhidraDocs/languages/html/pcoderef.html>`_