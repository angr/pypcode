#!/usr/bin/env python
"""
Pythonic interface to SLEIGH by way of the csleigh C API wrapper and CFFI.

.. include:: ../README.md
"""

import os.path
import xml.etree.ElementTree as ET
from enum import Enum
from typing import TYPE_CHECKING, Generator, Sequence, Optional, Mapping, Union, Tuple

from ._csleigh import ffi
from ._csleigh.lib import (
    csleigh_Addr_getSpaceFromConst,
    csleigh_Addr_isConstant,
    csleigh_AddrSpace_getName,
    csleigh_CPUI_BOOL_AND,
    csleigh_CPUI_BOOL_NEGATE,
    csleigh_CPUI_BOOL_OR,
    csleigh_CPUI_BOOL_XOR,
    csleigh_CPUI_BRANCH,
    csleigh_CPUI_BRANCHIND,
    csleigh_CPUI_CALL,
    csleigh_CPUI_CALLIND,
    csleigh_CPUI_CALLOTHER,
    csleigh_CPUI_CAST,
    csleigh_CPUI_CBRANCH,
    csleigh_CPUI_COPY,
    csleigh_CPUI_CPOOLREF,
    csleigh_CPUI_EXTRACT,
    csleigh_CPUI_FLOAT_ABS,
    csleigh_CPUI_FLOAT_ADD,
    csleigh_CPUI_FLOAT_CEIL,
    csleigh_CPUI_FLOAT_DIV,
    csleigh_CPUI_FLOAT_EQUAL,
    csleigh_CPUI_FLOAT_FLOAT2FLOAT,
    csleigh_CPUI_FLOAT_FLOOR,
    csleigh_CPUI_FLOAT_INT2FLOAT,
    csleigh_CPUI_FLOAT_LESS,
    csleigh_CPUI_FLOAT_LESSEQUAL,
    csleigh_CPUI_FLOAT_MULT,
    csleigh_CPUI_FLOAT_NAN,
    csleigh_CPUI_FLOAT_NEG,
    csleigh_CPUI_FLOAT_NOTEQUAL,
    csleigh_CPUI_FLOAT_ROUND,
    csleigh_CPUI_FLOAT_SQRT,
    csleigh_CPUI_FLOAT_SUB,
    csleigh_CPUI_FLOAT_TRUNC,
    csleigh_CPUI_INDIRECT,
    csleigh_CPUI_INSERT,
    csleigh_CPUI_INT_2COMP,
    csleigh_CPUI_INT_ADD,
    csleigh_CPUI_INT_AND,
    csleigh_CPUI_INT_CARRY,
    csleigh_CPUI_INT_DIV,
    csleigh_CPUI_INT_EQUAL,
    csleigh_CPUI_INT_LEFT,
    csleigh_CPUI_INT_LESS,
    csleigh_CPUI_INT_LESSEQUAL,
    csleigh_CPUI_INT_MULT,
    csleigh_CPUI_INT_NEGATE,
    csleigh_CPUI_INT_NOTEQUAL,
    csleigh_CPUI_INT_OR,
    csleigh_CPUI_INT_REM,
    csleigh_CPUI_INT_RIGHT,
    csleigh_CPUI_INT_SBORROW,
    csleigh_CPUI_INT_SCARRY,
    csleigh_CPUI_INT_SDIV,
    csleigh_CPUI_INT_SEXT,
    csleigh_CPUI_INT_SLESS,
    csleigh_CPUI_INT_SLESSEQUAL,
    csleigh_CPUI_INT_SREM,
    csleigh_CPUI_INT_SRIGHT,
    csleigh_CPUI_INT_SUB,
    csleigh_CPUI_INT_XOR,
    csleigh_CPUI_INT_ZEXT,
    csleigh_CPUI_LOAD,
    csleigh_CPUI_MULTIEQUAL,
    csleigh_CPUI_NEW,
    csleigh_CPUI_PIECE,
    csleigh_CPUI_POPCOUNT,
    csleigh_CPUI_PTRADD,
    csleigh_CPUI_PTRSUB,
    csleigh_CPUI_RETURN,
    csleigh_CPUI_SEGMENTOP,
    csleigh_CPUI_STORE,
    csleigh_CPUI_SUBPIECE,
    csleigh_createContext,
    csleigh_destroyContext,
    csleigh_ERROR_TYPE_BADDATA,
    csleigh_ERROR_TYPE_GENERIC,
    csleigh_ERROR_TYPE_NOERROR,
    csleigh_ERROR_TYPE_UNIMPL,
    csleigh_freeResult,
    csleigh_setVariableDefault,
    csleigh_Sleigh_getAllRegisters,
    csleigh_Sleigh_getRegisterName,
    csleigh_translate,
)

if TYPE_CHECKING:
    csleigh_Address = ffi.CData
    csleigh_AddrSpace = ffi.CData
    csleigh_Context = ffi.CData
    csleigh_Error = ffi.CData
    csleigh_PcodeOp = ffi.CData
    csleigh_SeqNum = ffi.CData
    csleigh_Translation = ffi.CData
    csleigh_TranslationResult = ffi.CData
    csleigh_Varnode = ffi.CData


PKG_SRC_DIR = os.path.abspath(os.path.dirname(__file__))
SPECFILES_DIR = os.path.join(PKG_SRC_DIR, "processors")


class OpCode(Enum):
    """
    1:1 mapping of C enumeration csleigh_CPUI_* to Enum
    """
    BOOL_AND = csleigh_CPUI_BOOL_AND
    BOOL_NEGATE = csleigh_CPUI_BOOL_NEGATE
    BOOL_OR = csleigh_CPUI_BOOL_OR
    BOOL_XOR = csleigh_CPUI_BOOL_XOR
    BRANCH = csleigh_CPUI_BRANCH
    BRANCHIND = csleigh_CPUI_BRANCHIND
    CALL = csleigh_CPUI_CALL
    CALLIND = csleigh_CPUI_CALLIND
    CALLOTHER = csleigh_CPUI_CALLOTHER
    CAST = csleigh_CPUI_CAST
    CBRANCH = csleigh_CPUI_CBRANCH
    COPY = csleigh_CPUI_COPY
    CPOOLREF = csleigh_CPUI_CPOOLREF
    EXTRACT = csleigh_CPUI_EXTRACT
    FLOAT_ABS = csleigh_CPUI_FLOAT_ABS
    FLOAT_ADD = csleigh_CPUI_FLOAT_ADD
    FLOAT_CEIL = csleigh_CPUI_FLOAT_CEIL
    FLOAT_DIV = csleigh_CPUI_FLOAT_DIV
    FLOAT_EQUAL = csleigh_CPUI_FLOAT_EQUAL
    FLOAT_FLOAT2FLOAT = csleigh_CPUI_FLOAT_FLOAT2FLOAT
    FLOAT_FLOOR = csleigh_CPUI_FLOAT_FLOOR
    FLOAT_INT2FLOAT = csleigh_CPUI_FLOAT_INT2FLOAT
    FLOAT_LESS = csleigh_CPUI_FLOAT_LESS
    FLOAT_LESSEQUAL = csleigh_CPUI_FLOAT_LESSEQUAL
    FLOAT_MULT = csleigh_CPUI_FLOAT_MULT
    FLOAT_NAN = csleigh_CPUI_FLOAT_NAN
    FLOAT_NEG = csleigh_CPUI_FLOAT_NEG
    FLOAT_NOTEQUAL = csleigh_CPUI_FLOAT_NOTEQUAL
    FLOAT_ROUND = csleigh_CPUI_FLOAT_ROUND
    FLOAT_SQRT = csleigh_CPUI_FLOAT_SQRT
    FLOAT_SUB = csleigh_CPUI_FLOAT_SUB
    FLOAT_TRUNC = csleigh_CPUI_FLOAT_TRUNC
    INDIRECT = csleigh_CPUI_INDIRECT
    INSERT = csleigh_CPUI_INSERT
    INT_2COMP = csleigh_CPUI_INT_2COMP
    INT_ADD = csleigh_CPUI_INT_ADD
    INT_AND = csleigh_CPUI_INT_AND
    INT_CARRY = csleigh_CPUI_INT_CARRY
    INT_DIV = csleigh_CPUI_INT_DIV
    INT_EQUAL = csleigh_CPUI_INT_EQUAL
    INT_LEFT = csleigh_CPUI_INT_LEFT
    INT_LESS = csleigh_CPUI_INT_LESS
    INT_LESSEQUAL = csleigh_CPUI_INT_LESSEQUAL
    INT_MULT = csleigh_CPUI_INT_MULT
    INT_NEGATE = csleigh_CPUI_INT_NEGATE
    INT_NOTEQUAL = csleigh_CPUI_INT_NOTEQUAL
    INT_OR = csleigh_CPUI_INT_OR
    INT_REM = csleigh_CPUI_INT_REM
    INT_RIGHT = csleigh_CPUI_INT_RIGHT
    INT_SBORROW = csleigh_CPUI_INT_SBORROW
    INT_SCARRY = csleigh_CPUI_INT_SCARRY
    INT_SDIV = csleigh_CPUI_INT_SDIV
    INT_SEXT = csleigh_CPUI_INT_SEXT
    INT_SLESS = csleigh_CPUI_INT_SLESS
    INT_SLESSEQUAL = csleigh_CPUI_INT_SLESSEQUAL
    INT_SREM = csleigh_CPUI_INT_SREM
    INT_SRIGHT = csleigh_CPUI_INT_SRIGHT
    INT_SUB = csleigh_CPUI_INT_SUB
    INT_XOR = csleigh_CPUI_INT_XOR
    INT_ZEXT = csleigh_CPUI_INT_ZEXT
    LOAD = csleigh_CPUI_LOAD
    MULTIEQUAL = csleigh_CPUI_MULTIEQUAL
    NEW = csleigh_CPUI_NEW
    PIECE = csleigh_CPUI_PIECE
    POPCOUNT = csleigh_CPUI_POPCOUNT
    PTRADD = csleigh_CPUI_PTRADD
    PTRSUB = csleigh_CPUI_PTRSUB
    RETURN = csleigh_CPUI_RETURN
    SEGMENTOP = csleigh_CPUI_SEGMENTOP
    STORE = csleigh_CPUI_STORE
    SUBPIECE = csleigh_CPUI_SUBPIECE


class SleighErrorType(Enum):
    """
    1:1 mapping of C enumeration csleigh_ERROR_TYPE_* to Enum
    """
    BADDATA = csleigh_ERROR_TYPE_BADDATA
    GENERIC = csleigh_ERROR_TYPE_GENERIC
    NOERROR = csleigh_ERROR_TYPE_NOERROR
    UNIMPL = csleigh_ERROR_TYPE_UNIMPL


class ArchLanguage:
    """
    A specific language for an architecture. Provides access to language, pspec, and cspecs.
    """

    __slots__ = (
        "archdir",
        "ldef",
        "_pspec",
        "_cspecs",
    )

    archdir: str
    ldef: ET.Element
    pspec: Optional[ET.Element]

    def __init__(self, archdir: str, ldef: ET.Element):
        self.archdir = archdir
        self.ldef = ldef
        self._pspec = None
        self._cspecs = None

    @property
    def pspec_path(self) -> str:
        return os.path.join(self.archdir, self.processorspec)

    @property
    def slafile_path(self) -> str:
        return os.path.join(self.archdir, self.slafile)

    @property
    def description(self) -> str:
        return self.ldef.find("description").text

    def __getattr__(self, key):
        if key in self.ldef.attrib:
            return self.ldef.attrib[key]
        raise AttributeError(key)

    @property
    def pspec(self) -> ET.Element:
        if self._pspec is None:
            self._pspec = ET.parse(self.pspec_path).getroot()
        return self._pspec

    @property
    def cspecs(self) -> Mapping[Tuple[str, str], ET.Element]:
        if self._cspecs is None:
            self._cspecs = {}
            for e in self.ldef.findall("compiler"):
                path = os.path.join(self.archdir, e.attrib["spec"])
                cspec = ET.parse(path).getroot()
                self._cspecs[(e.attrib["id"], e.attrib["name"])] = cspec
        return self._cspecs

    def init_context_from_pspec(self, ctx: "csleigh_Context") -> None:
        cd = self.pspec.find("context_data")
        if cd is None:
            return
        cs = cd.find("context_set")
        if cs is None:
            return
        for e in cs:
            assert e.tag == "set"
            csleigh_setVariableDefault(ctx, e.attrib["name"].encode("utf-8"), int(e.attrib["val"]))


class Arch:
    """
    Main class representing an architecture describing available languages.
    """

    __slots__ = (
        "archpath",
        "archname",
        "ldefpath",
        "ldef",
        "languages",
    )

    archpath: str
    archname: str
    ldefpath: str
    ldef: ET.ElementTree
    languages: Sequence[ArchLanguage]

    def __init__(self, archname: str, ldefpath: str):
        self.archpath = os.path.dirname(ldefpath)
        self.archname = archname
        self.ldefpath = ldefpath
        self.ldef = ET.parse(ldefpath)
        self.languages = [ArchLanguage(self.archpath, e) for e in self.ldef.getroot()]

    @classmethod
    def enumerate(cls) -> Generator["Arch", None, None]:
        """
        Enumerate all available architectures and languages.

        Language definitions are sourced from definitions shipped with pypcode and
        can be found in processors/<architecture>/data/languages/<variant>.ldefs
        """
        for archname in os.listdir(SPECFILES_DIR):
            langdir = os.path.join(SPECFILES_DIR, archname, "data", "languages")
            if not (os.path.exists(langdir) and os.path.isdir(langdir)):
                continue
            for langname in os.listdir(langdir):
                if not langname.endswith(".ldefs"):
                    continue
                ldefpath = os.path.join(langdir, langname)
                yield Arch(archname, ldefpath)


class Context:
    """
    Context for translation.
    """

    __slots__ = (
        "lang",
        "ctx_c",
        "_cached_addr_spaces",
        "registers",
    )

    lang: ArchLanguage
    ctx_c: "csleigh_Context"
    _cached_addr_spaces: Mapping["csleigh_AddrSpace", "AddrSpace"]

    def __init__(self, lang: ArchLanguage):
        self._cached_addr_spaces = {}
        self.lang = lang
        self.ctx_c = csleigh_createContext(self.lang.slafile_path.encode("utf-8"))
        self.lang.init_context_from_pspec(self.ctx_c)

        count_a = ffi.new("unsigned int *count")
        regs = csleigh_Sleigh_getAllRegisters(self.ctx_c, count_a)

        self.registers = {}
        for i in range(count_a[0]):
            reg_name = ffi.string(regs[i].name).decode("utf-8")
            reg_vn = Varnode.from_c(self, regs[i].varnode)
            self.registers[reg_name] = reg_vn

    def __del__(self):
        csleigh_destroyContext(self.ctx_c)

    def get_cached_addr_space(self, cobj: "csleigh_AddrSpace") -> "AddrSpace":
        """
        Used during translation to cache unchanging address space objects. Should
        not be called by pypcode users.
        """
        return self._cached_addr_spaces.get(cobj)

    def set_cached_addr_space(self, cobj: "csleigh_AddrSpace", pobj: "AddrSpace") -> None:
        """
        Used during translation to cache unchanging address space objects. Should
        not be called by pypcode users.
        """
        self._cached_addr_spaces[cobj] = pobj

    def translate(
        self,
        code: Union[bytes, bytearray],
        base: int,
        max_inst: int = 0,
        max_bytes: int = 0,
        bb_terminating: bool = False,
    ) -> "TranslationResult":
        """
        Disassemble and translate to p-code.

        :param code:           Buffer of machine code to translate
        :param base:           Base address of the machine code
        :param max_inst:       Maximum number of instructions to translate, or 0 for no limit
        :param max_bytes:      Maximum number of bytes to translate, or 0 for no limit
        :param bb_terminating: End translation at basic block boundaries
        """
        c_data = ffi.from_buffer(code)
        max_bytes = min(len(code), max_bytes) if (max_bytes > 0) else len(code)
        res_c = csleigh_translate(self.ctx_c, c_data, max_bytes, base, max_inst, bb_terminating)
        res = TranslationResult.from_c(self, res_c)
        csleigh_freeResult(res_c)
        return res

    def get_register_name(self, space: "AddrSpace", offset: int, size: int) -> str:
        """
        Call SleighBase::getRegisterName in this context.
        """
        return ffi.string(csleigh_Sleigh_getRegisterName(self.ctx_c, space.to_c(), offset, size)).decode("utf-8")


class ContextObj:
    """
    Base class for objects that are context-sensitive.
    """

    __slots__ = ("ctx",)

    ctx: Context

    def __init__(self, ctx: Context):
        self.ctx = ctx


class AddrSpace(ContextObj):
    """
    An address space.
    """

    __slots__ = (
        "cobj",
        "name",
    )

    cobj: "csleigh_AddrSpace"
    name: str

    def __init__(self, ctx: Context, cobj: "csleigh_AddrSpace"):
        super().__init__(ctx)
        self.cobj = cobj
        self.name = ffi.string(csleigh_AddrSpace_getName(cobj)).decode("utf-8")

    @classmethod
    def from_c_uncached(cls, ctx: Context, cobj: "csleigh_AddrSpace") -> "AddrSpace":
        return cls(ctx, cobj)

    @classmethod
    def from_c(cls, ctx: Context, cobj: "csleigh_AddrSpace") -> "AddrSpace":
        obj = ctx.get_cached_addr_space(cobj)
        if obj is None:
            obj = cls.from_c_uncached(ctx, cobj)
            ctx.set_cached_addr_space(cobj, obj)
        return obj

    def to_c(self) -> "csleigh_AddrSpace":
        return self.cobj


class Address(ContextObj):
    """
    Addresses a byte within some address space.
    """

    __slots__ = (
        "space",
        "offset",
    )

    space: AddrSpace
    offset: int

    def __init__(self, ctx: Context, space: AddrSpace, offset: int):
        super().__init__(ctx)
        self.space = space
        self.offset = offset

    @classmethod
    def from_c(cls, ctx: Context, cobj: "csleigh_Address") -> "Address":
        return cls(ctx, AddrSpace.from_c(ctx, cobj.space), cobj.offset)

    def to_c(self) -> "csleigh_Address":
        # XXX: The boxing in AddrSpace/Address is a little excessive, but lets us
        # access the API as provided by SLEIGH, and should still be fast.
        cobj = ffi.new("csleigh_Address *")
        cobj.space = self.space.to_c()
        cobj.offset = self.offset
        return cobj

    @property
    def is_constant(self) -> bool:
        """
        Return True if this address is in the constant space.
        """
        return csleigh_Addr_isConstant(self.to_c())

    def get_space_from_const(self) -> AddrSpace:
        """
        For LOAD/STORE, the address space which is being accessed is encoded as
        a pointer stored in a constant space offset. See Address::getSpaceFromConst.
        """
        return AddrSpace.from_c(self.ctx, csleigh_Addr_getSpaceFromConst(self.to_c()))


class Varnode(ContextObj):
    """
    Data manipulated by p-code.
    """

    __slots__ = (
        "space",
        "offset",
        "size",
    )

    space: AddrSpace
    offset: int
    size: int

    def __init__(self, ctx: Context, space: AddrSpace, offset: int, size: int):
        super().__init__(ctx)
        self.space = space
        self.offset = offset
        self.size = size

    @classmethod
    def from_c(cls, ctx: Context, cobj: "csleigh_Varnode") -> "Varnode":
        return cls(ctx, AddrSpace.from_c(ctx, cobj.space), cobj.offset, cobj.size)

    def __str__(self):
        return "%s[%#x:%d]" % (self.space.name, self.offset, self.size)

    def get_addr(self) -> Address:
        return Address(self.ctx, self.space, self.offset)

    def get_register_name(self) -> str:
        """
        Convenience function to call SleighBase::getRegisterName with current
        Varnode attributes.
        """
        return self.ctx.get_register_name(self.space, self.offset, self.size)

    def get_space_from_const(self) -> AddrSpace:
        """
        Convenience function to call Address::getSpaceFromConst with current Varnode
        attributes.
        """
        return self.get_addr().get_space_from_const()


class SeqNum(ContextObj):
    """
    Unique address for p-code ops translated from an instruction at `pc`.
    """

    __slots__ = (
        "pc",
        "uniq",
        "order",
    )

    pc: Address
    uniq: int
    order: int

    def __init__(self, ctx: Context, pc: Address, uniq: int, order: int):
        super().__init__(ctx)
        self.pc = pc
        self.uniq = uniq
        self.order = order

    @classmethod
    def from_c(cls, ctx: Context, cobj: "csleigh_SeqNum") -> "SeqNum":
        return cls(ctx, Address.from_c(ctx, cobj.pc), cobj.uniq, cobj.order)


class PcodeOp(ContextObj):
    """
    A single p-code op.
    """

    __slots__ = (
        "seq",
        "opcode",
        "output",
        "inputs",
    )

    seq: SeqNum
    opcode: OpCode
    output: Optional[Varnode]
    inputs: Sequence[Varnode]

    def __init__(
        self,
        ctx: Context,
        seq: SeqNum,
        opcode: OpCode,
        inputs: Sequence[Varnode],
        output: Optional[Varnode] = None,
    ):
        super().__init__(ctx)
        self.seq = seq
        self.opcode = opcode
        self.output = output
        self.inputs = inputs

    @classmethod
    def from_c(cls, ctx: Context, cobj: "csleigh_PcodeOp") -> "PcodeOp":
        return cls(
            ctx,
            SeqNum.from_c(ctx, cobj.seq),
            OpCode(cobj.opcode),
            [Varnode.from_c(ctx, cobj.inputs[i]) for i in range(cobj.inputs_count)],
            Varnode.from_c(ctx, cobj.output) if cobj.output else None,
        )

    def __str__(self):
        s = ""
        if self.output:
            s += str(self.output) + " = "
        s += f'{self.opcode.name} {", ".join(str(i) for i in self.inputs)}'
        return s


class OpFormat:
    """
    General op pretty-printer.
    """

    @staticmethod
    def fmt_vn(vn: Varnode) -> str:
        if vn.space.name == "const":
            return "%#x" % vn.offset
        elif vn.space.name == "register":
            name = vn.get_register_name()
            if name:
                return name
        return str(vn)

    def fmt(self, op: PcodeOp) -> str:
        return f'{op.opcode.name} {", ".join(self.fmt_vn(i) for i in op.inputs)}'


class OpFormatUnary(OpFormat):
    """
    General unary op pretty-printer.
    """

    __slots__ = ("operator",)

    def __init__(self, operator: str):
        super().__init__()
        self.operator = operator

    def fmt(self, op: PcodeOp) -> str:
        return f"{self.operator}{self.fmt_vn(op.inputs[0])}"


class OpFormatBinary(OpFormat):
    """
    General binary op pretty-printer.
    """

    __slots__ = ("operator",)

    def __init__(self, operator: str):
        super().__init__()
        self.operator = operator

    def fmt(self, op: PcodeOp) -> str:
        return f"{self.fmt_vn(op.inputs[0])} {self.operator} {self.fmt_vn(op.inputs[1])}"


class OpFormatFunc(OpFormat):
    """
    Function-call style op pretty-printer.
    """

    __slots__ = ("operator",)

    def __init__(self, operator: str):
        super().__init__()
        self.operator = operator

    def fmt(self, op: PcodeOp) -> str:
        return f'{self.operator}({", ".join(self.fmt_vn(i) for i in op.inputs)})'


class OpFormatSpecial(OpFormat):
    """
    Specialized op pretty-printers.
    """

    def fmt_BRANCH(self, op: PcodeOp) -> str:
        return f"goto {self.fmt_vn(op.inputs[0])}"

    def fmt_BRANCHIND(self, op: PcodeOp) -> str:
        return f"goto [{self.fmt_vn(op.inputs[0])}]"

    def fmt_CALL(self, op: PcodeOp) -> str:
        return f"call {self.fmt_vn(op.inputs[0])}"

    def fmt_CALLIND(self, op: PcodeOp) -> str:
        return f"call [{self.fmt_vn(op.inputs[0])}]"

    def fmt_CBRANCH(self, op: PcodeOp) -> str:
        return f"if ({self.fmt_vn(op.inputs[1])}) goto {self.fmt_vn(op.inputs[0])}"

    def fmt_LOAD(self, op: PcodeOp) -> str:
        return f"*[{op.inputs[0].get_space_from_const().name}]{self.fmt_vn(op.inputs[1])}"

    def fmt_RETURN(self, op: PcodeOp) -> str:
        return f"return {self.fmt_vn(op.inputs[0])}"

    def fmt_STORE(self, op: PcodeOp) -> str:
        return f"*[{op.inputs[0].get_space_from_const().name}]{self.fmt_vn(op.inputs[1])} = {op.inputs[2]}"

    def fmt(self, op: PcodeOp) -> str:
        return {
            OpCode.BRANCH: self.fmt_BRANCH,
            OpCode.BRANCHIND: self.fmt_BRANCHIND,
            OpCode.CALL: self.fmt_CALL,
            OpCode.CALLIND: self.fmt_CALLIND,
            OpCode.CBRANCH: self.fmt_CBRANCH,
            OpCode.LOAD: self.fmt_LOAD,
            OpCode.RETURN: self.fmt_RETURN,
            OpCode.STORE: self.fmt_STORE,
        }.get(op.opcode)(op)


class PcodePrettyPrinter:
    """
    P-code pretty-printer.
    """

    DEFAULT_OP_FORMAT = OpFormat()

    OP_FORMATS = {
        OpCode.BOOL_AND: OpFormatBinary("&&"),
        OpCode.BOOL_NEGATE: OpFormatUnary("!"),
        OpCode.BOOL_OR: OpFormatBinary("||"),
        OpCode.BOOL_XOR: OpFormatBinary("^^"),
        OpCode.BRANCH: OpFormatSpecial(),
        OpCode.BRANCHIND: OpFormatSpecial(),
        OpCode.CALL: OpFormatSpecial(),
        OpCode.CALLIND: OpFormatSpecial(),
        OpCode.CBRANCH: OpFormatSpecial(),
        OpCode.COPY: OpFormatUnary(""),
        OpCode.CPOOLREF: OpFormatFunc("cpool"),
        OpCode.FLOAT_ABS: OpFormatFunc("abs"),
        OpCode.FLOAT_ADD: OpFormatBinary("f+"),
        OpCode.FLOAT_CEIL: OpFormatFunc("ceil"),
        OpCode.FLOAT_DIV: OpFormatBinary("f/"),
        OpCode.FLOAT_EQUAL: OpFormatBinary("f=="),
        OpCode.FLOAT_FLOAT2FLOAT: OpFormatFunc("float2float"),
        OpCode.FLOAT_FLOOR: OpFormatFunc("floor"),
        OpCode.FLOAT_INT2FLOAT: OpFormatFunc("int2float"),
        OpCode.FLOAT_LESS: OpFormatBinary("f<"),
        OpCode.FLOAT_LESSEQUAL: OpFormatBinary("f<="),
        OpCode.FLOAT_MULT: OpFormatBinary("f*"),
        OpCode.FLOAT_NAN: OpFormatFunc("nan"),
        OpCode.FLOAT_NEG: OpFormatUnary("f- "),
        OpCode.FLOAT_NOTEQUAL: OpFormatBinary("f!="),
        OpCode.FLOAT_ROUND: OpFormatFunc("round"),
        OpCode.FLOAT_SQRT: OpFormatFunc("sqrt"),
        OpCode.FLOAT_SUB: OpFormatBinary("f-"),
        OpCode.FLOAT_TRUNC: OpFormatFunc("trunc"),
        OpCode.INT_2COMP: OpFormatUnary("-"),
        OpCode.INT_ADD: OpFormatBinary("+"),
        OpCode.INT_AND: OpFormatBinary("&"),
        OpCode.INT_CARRY: OpFormatFunc("carry"),
        OpCode.INT_DIV: OpFormatBinary("/"),
        OpCode.INT_EQUAL: OpFormatBinary("=="),
        OpCode.INT_LEFT: OpFormatBinary("<<"),
        OpCode.INT_LESS: OpFormatBinary("<"),
        OpCode.INT_LESSEQUAL: OpFormatBinary("<="),
        OpCode.INT_MULT: OpFormatBinary("*"),
        OpCode.INT_NEGATE: OpFormatUnary("~"),
        OpCode.INT_NOTEQUAL: OpFormatBinary("!="),
        OpCode.INT_OR: OpFormatBinary("|"),
        OpCode.INT_REM: OpFormatBinary("%"),
        OpCode.INT_RIGHT: OpFormatBinary(">>"),
        OpCode.INT_SBORROW: OpFormatFunc("sborrow"),
        OpCode.INT_SCARRY: OpFormatFunc("scarry"),
        OpCode.INT_SDIV: OpFormatBinary("s/"),
        OpCode.INT_SEXT: OpFormatFunc("sext"),
        OpCode.INT_SLESS: OpFormatBinary("s<"),
        OpCode.INT_SLESSEQUAL: OpFormatBinary("s<="),
        OpCode.INT_SREM: OpFormatBinary("s%"),
        OpCode.INT_SRIGHT: OpFormatBinary("s>>"),
        OpCode.INT_SUB: OpFormatBinary("-"),
        OpCode.INT_XOR: OpFormatBinary("^"),
        OpCode.INT_ZEXT: OpFormatFunc("zext"),
        OpCode.LOAD: OpFormatSpecial(),
        OpCode.NEW: OpFormatFunc("newobject"),
        OpCode.POPCOUNT: OpFormatFunc("popcount"),
        OpCode.RETURN: OpFormatSpecial(),
        OpCode.STORE: OpFormatSpecial(),
    }

    @classmethod
    def fmt_op(cls, op: PcodeOp) -> str:
        fmt = cls.OP_FORMATS.get(op.opcode, cls.DEFAULT_OP_FORMAT)
        return (f"{fmt.fmt_vn(op.output)} = " if op.output else "") + fmt.fmt(op)


class Translation(ContextObj):
    """
    Translation of a machine instruction to p-code.
    """

    __slots__ = (
        "address",
        "length",
        "asm_mnem",
        "asm_body",
        "ops",
    )

    address: Address
    length: int
    asm_mnem: str
    asm_body: str
    ops: Sequence[PcodeOp]

    def __init__(
        self,
        ctx: Context,
        address: Address,
        length: int,
        asm_mnem: str,
        asm_body: str,
        ops: Sequence[PcodeOp],
    ):
        super().__init__(ctx)
        self.address = address
        self.length = length
        self.asm_mnem = asm_mnem
        self.asm_body = asm_body
        self.ops = ops

    @classmethod
    def from_c(cls, ctx: Context, cobj: "csleigh_Translation") -> "Translation":
        return cls(
            ctx,
            Address.from_c(ctx, cobj.address),
            cobj.length,
            ffi.string(cobj.asm_mnem).decode("utf-8"),
            ffi.string(cobj.asm_body).decode("utf-8"),
            [PcodeOp.from_c(ctx, cobj.ops[i]) for i in range(cobj.ops_count)],
        )


class SleighError(Exception):
    """
    Base class for translation errors.
    """

    __slots__ = ("ctx",)

    ctx: Context

    def __init__(self, ctx: Context, explain: str):
        super().__init__(explain)
        self.ctx = ctx


class UnimplError(SleighError):
    """
    UnimplError exception.
    """

    __slots__ = (
        "explain",
        "address",
        "instruction_length",
    )

    explain: str
    address: Address
    instruction_length: int

    def __init__(self, ctx: Context, explain: str, address: Address, instruction_length: int):
        super().__init__(ctx, explain)
        self.explain = explain
        self.address = address
        self.instruction_length = instruction_length

    @classmethod
    def from_c(cls, ctx: Context, cobj: "csleigh_Error") -> "UnimplError":
        assert SleighErrorType(cobj.type) == SleighErrorType.UNIMPL
        return cls(
            ctx,
            ffi.string(cobj.explain).decode("utf-8"),
            Address.from_c(ctx, cobj.unimpl.address),
            cobj.unimpl.instruction_length,
        )


class BadDataError(SleighError):
    """
    BadDataError exception.
    """

    __slots__ = (
        "explain",
        "address",
    )

    explain: str
    address: Address

    def __init__(self, ctx: Context, explain: str, address: Address):
        super().__init__(ctx, explain)
        self.explain = explain
        self.address = address

    @classmethod
    def from_c(cls, ctx: Context, cobj: "csleigh_Error") -> "BadDataError":
        assert SleighErrorType(cobj.type) == SleighErrorType.BADDATA
        return cls(
            ctx,
            ffi.string(cobj.explain).decode("utf-8"),
            Address.from_c(ctx, cobj.unimpl.address),
        )


class SleighErrorFactory:
    """
    Generates SleighErrorType objects from csleigh errors.
    """

    @classmethod
    def from_c(cls, ctx: Context, cobj: "csleigh_Error") -> Union[None, UnimplError, BadDataError]:
        t = SleighErrorType(cobj.type)
        if t == SleighErrorType.NOERROR:
            return None
        else:
            return {SleighErrorType.UNIMPL: UnimplError, SleighErrorType.BADDATA: BadDataError,}[
                t
            ].from_c(ctx, cobj)


class TranslationResult(ContextObj):
    """
    The result of a translation.
    """

    __slots__ = (
        "instructions",
        "error",
    )

    instructions: Sequence[Translation]
    error: SleighError

    def __init__(
        self,
        ctx: Context,
        instructions: Sequence[Translation],
        error: Optional[SleighError] = None,
    ):
        super().__init__(ctx)
        self.instructions = instructions
        self.error = error

    @classmethod
    def from_c(cls, ctx: Context, cobj: "csleigh_TranslationResult") -> "TranslationResult":
        return cls(
            ctx,
            [Translation.from_c(ctx, cobj.instructions[i]) for i in range(cobj.instructions_count)],
            SleighErrorFactory.from_c(ctx, cobj.error),
        )
