#!/usr/bin/env python
"""
Pythonic interface to SLEIGH
"""

import os.path
import xml.etree.ElementTree as ET
from enum import IntEnum
from typing import cast, Dict, Generator, Sequence, Optional, Mapping, Tuple, Union

from .__version__ import __version__

from .pypcode_native import __version__ as __pypcode_native_version__  # pylint:disable=no-name-in-module

assert __version__ == __pypcode_native_version__

from .pypcode_native import (  # pylint:disable=no-name-in-module
    Address,
    AddrSpace,
    BadDataError,
    DecoderError,
    Disassembly,
    Instruction,
    LowlevelError,
    OpCode,
    PcodeOp,
    TRANSLATE_FLAGS_BB_TERMINATING,
    Translation,
    UnimplError,
    Varnode,
)

from .pypcode_native import Context as _Context  # pylint:disable=no-name-in-module


__all__ = [
    "Address",
    "AddrSpace",
    "Arch",
    "ArchLanguage",
    "BadDataError",
    "Context",
    "DecoderError",
    "Disassembly",
    "Instruction",
    "LowlevelError",
    "OpCode",
    "OpFormat",
    "OpFormatBinary",
    "OpFormatFunc",
    "OpFormatSpecial",
    "OpFormatUnary",
    "PcodeOp",
    "PcodePrettyPrinter",
    "TranslateFlags",
    "Translation",
    "UnimplError",
    "Varnode",
]


class TranslateFlags(IntEnum):
    """
    Flags that can be passed to Context::translate
    """

    BB_TERMINATING = TRANSLATE_FLAGS_BB_TERMINATING


PKG_SRC_DIR = os.path.abspath(os.path.dirname(__file__))
SPECFILES_DIR = os.path.join(PKG_SRC_DIR, "processors")


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

    def __init__(self, archdir: str, ldef: ET.Element):
        self.archdir = archdir
        self.ldef = ldef
        self._pspec: Optional[ET.Element] = None
        self._cspecs: Optional[Dict[Tuple[str, str], ET.Element]] = None

    @property
    def pspec_path(self) -> str:
        return os.path.join(self.archdir, self.processorspec)

    @property
    def slafile_path(self) -> str:
        return os.path.join(self.archdir, self.slafile)

    @property
    def description(self) -> str:
        elem = self.ldef.find("description")
        if elem is not None:
            return elem.text or ""
        return ""

    def __getattr__(self, key):
        if key in self.ldef.attrib:
            return self.ldef.attrib[key]
        raise AttributeError(key)

    @property
    def pspec(self) -> Optional[ET.Element]:
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

    def init_context_from_pspec(self, ctx: "Context") -> None:
        if self.pspec is None:
            return
        cd = self.pspec.find("context_data")
        if cd is None:
            return
        cs = cd.find("context_set")
        if cs is None:
            return
        for e in cs:
            assert e.tag == "set"
            ctx.setVariableDefault(e.attrib["name"], int(e.attrib["val"]))

    @classmethod
    def from_id(cls, langid: str) -> Optional["ArchLanguage"]:
        """
        Return language with given id, or None if the language could not be found.
        """
        for arch in Arch.enumerate():
            for lang in arch.languages:
                if lang.id == langid:
                    return lang
        return None


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

    def __init__(self, name: str, ldefpath: str):
        """
        Initialize the Arch.

        :param name: The name of the architecture
        :param ldefpath: Path to language definition files (.ldefs)
        """
        self.archpath = os.path.dirname(ldefpath)
        self.archname = name
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


class Context(_Context):
    """
    Context for translation.
    """

    __slots__ = (
        "language",
        "registers",
    )

    language: ArchLanguage
    registers: Dict[str, Varnode]

    def __init__(self, language: Union[ArchLanguage, str]):
        """
        Initialize a context for translation or disassembly.

        :param language: The ``ArchLanguage`` to initialize the context with, or a language id ``str``
        """
        if isinstance(language, ArchLanguage):
            self.language = language
        elif isinstance(language, str):
            _l = ArchLanguage.from_id(cast(str, language))
            assert _l is not None
            self.language = _l
        else:
            assert False, "Context must be initialized with a language or language id"
        super().__init__(self.language.slafile_path)
        self.language.init_context_from_pspec(self)
        self.registers = {n: v for v, n in self.getAllRegisters().items()}


class OpFormat:
    """
    General op pretty-printer.
    """

    @staticmethod
    def fmt_vn(vn: Varnode) -> str:
        if vn.space.name == "const":
            return "%#x" % vn.offset
        elif vn.space.name == "register":
            name = vn.getRegisterName()
            if name:
                return name
        return f"{vn.space.name}[{vn.offset:x}:{vn.size:d}]"

    def fmt(self, op: PcodeOp) -> str:
        return f'{op.opcode.__name__} {", ".join(self.fmt_vn(i) for i in op.inputs)}'


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
        return f"*[{op.inputs[0].getSpaceFromConst().name}]{self.fmt_vn(op.inputs[1])}"

    def fmt_RETURN(self, op: PcodeOp) -> str:
        return f"return {self.fmt_vn(op.inputs[0])}"

    def fmt_STORE(self, op: PcodeOp) -> str:
        return f"*[{op.inputs[0].getSpaceFromConst().name}]{self.fmt_vn(op.inputs[1])} = {self.fmt_vn(op.inputs[2])}"

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
        }.get(op.opcode, super().fmt)(op)


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
        OpCode.LZCOUNT: OpFormatFunc("lzcount"),
        OpCode.RETURN: OpFormatSpecial(),
        OpCode.STORE: OpFormatSpecial(),
    }

    @classmethod
    def fmt_op(cls, op: PcodeOp) -> str:
        fmt = cls.OP_FORMATS.get(op.opcode, cls.DEFAULT_OP_FORMAT)
        return (f"{fmt.fmt_vn(op.output)} = " if op.output else "") + fmt.fmt(op)
