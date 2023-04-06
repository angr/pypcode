from typing import Any, ClassVar, List, Optional

__version__: str

TRANSLATE_FLAGS_BB_TERMINATING: int

class BadDataError(Exception): ...
class DecoderError(Exception): ...
class UnimplError(Exception): ...

class AddrSpace:
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def name(self) -> str: ...

class Address:
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def offset(self) -> int: ...
    @property
    def space(self) -> AddrSpace: ...

class Instruction:
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def addr(self) -> Address: ...
    @property
    def body(self) -> str: ...
    @property
    def length(self) -> int: ...
    @property
    def mnem(self) -> str: ...

class Disassembly:
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def instructions(self) -> List[Instruction]: ...

class OpCode:
    BOOL_AND: ClassVar[OpCode] = ...
    BOOL_NEGATE: ClassVar[OpCode] = ...
    BOOL_OR: ClassVar[OpCode] = ...
    BOOL_XOR: ClassVar[OpCode] = ...
    BRANCH: ClassVar[OpCode] = ...
    BRANCHIND: ClassVar[OpCode] = ...
    CALL: ClassVar[OpCode] = ...
    CALLIND: ClassVar[OpCode] = ...
    CALLOTHER: ClassVar[OpCode] = ...
    CAST: ClassVar[OpCode] = ...
    CBRANCH: ClassVar[OpCode] = ...
    COPY: ClassVar[OpCode] = ...
    CPOOLREF: ClassVar[OpCode] = ...
    EXTRACT: ClassVar[OpCode] = ...
    FLOAT_ABS: ClassVar[OpCode] = ...
    FLOAT_ADD: ClassVar[OpCode] = ...
    FLOAT_CEIL: ClassVar[OpCode] = ...
    FLOAT_DIV: ClassVar[OpCode] = ...
    FLOAT_EQUAL: ClassVar[OpCode] = ...
    FLOAT_FLOAT2FLOAT: ClassVar[OpCode] = ...
    FLOAT_FLOOR: ClassVar[OpCode] = ...
    FLOAT_INT2FLOAT: ClassVar[OpCode] = ...
    FLOAT_LESS: ClassVar[OpCode] = ...
    FLOAT_LESSEQUAL: ClassVar[OpCode] = ...
    FLOAT_MULT: ClassVar[OpCode] = ...
    FLOAT_NAN: ClassVar[OpCode] = ...
    FLOAT_NEG: ClassVar[OpCode] = ...
    FLOAT_NOTEQUAL: ClassVar[OpCode] = ...
    FLOAT_ROUND: ClassVar[OpCode] = ...
    FLOAT_SQRT: ClassVar[OpCode] = ...
    FLOAT_SUB: ClassVar[OpCode] = ...
    FLOAT_TRUNC: ClassVar[OpCode] = ...
    IMARK: ClassVar[OpCode] = ...
    INDIRECT: ClassVar[OpCode] = ...
    INSERT: ClassVar[OpCode] = ...
    INT_2COMP: ClassVar[OpCode] = ...
    INT_ADD: ClassVar[OpCode] = ...
    INT_AND: ClassVar[OpCode] = ...
    INT_CARRY: ClassVar[OpCode] = ...
    INT_DIV: ClassVar[OpCode] = ...
    INT_EQUAL: ClassVar[OpCode] = ...
    INT_LEFT: ClassVar[OpCode] = ...
    INT_LESS: ClassVar[OpCode] = ...
    INT_LESSEQUAL: ClassVar[OpCode] = ...
    INT_MULT: ClassVar[OpCode] = ...
    INT_NEGATE: ClassVar[OpCode] = ...
    INT_NOTEQUAL: ClassVar[OpCode] = ...
    INT_OR: ClassVar[OpCode] = ...
    INT_REM: ClassVar[OpCode] = ...
    INT_RIGHT: ClassVar[OpCode] = ...
    INT_SBORROW: ClassVar[OpCode] = ...
    INT_SCARRY: ClassVar[OpCode] = ...
    INT_SDIV: ClassVar[OpCode] = ...
    INT_SEXT: ClassVar[OpCode] = ...
    INT_SLESS: ClassVar[OpCode] = ...
    INT_SLESSEQUAL: ClassVar[OpCode] = ...
    INT_SREM: ClassVar[OpCode] = ...
    INT_SRIGHT: ClassVar[OpCode] = ...
    INT_SUB: ClassVar[OpCode] = ...
    INT_XOR: ClassVar[OpCode] = ...
    INT_ZEXT: ClassVar[OpCode] = ...
    LOAD: ClassVar[OpCode] = ...
    MULTIEQUAL: ClassVar[OpCode] = ...
    NEW: ClassVar[OpCode] = ...
    PIECE: ClassVar[OpCode] = ...
    POPCOUNT: ClassVar[OpCode] = ...
    PTRADD: ClassVar[OpCode] = ...
    PTRSUB: ClassVar[OpCode] = ...
    RETURN: ClassVar[OpCode] = ...
    SEGMENTOP: ClassVar[OpCode] = ...
    STORE: ClassVar[OpCode] = ...
    SUBPIECE: ClassVar[OpCode] = ...
    __entries: ClassVar[dict] = ...
    __name__: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __index__(self) -> Any: ...
    def __int__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...

class Varnode:
    def __init__(self) -> None: ...
    def getRegisterName(self) -> str: ...
    def getSpaceFromConst(self) -> AddrSpace: ...
    @property
    def offset(self) -> int: ...
    @property
    def size(self) -> int: ...
    @property
    def space(self) -> AddrSpace: ...

class PcodeOp:
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def inputs(self) -> List[Varnode]: ...
    @property
    def opcode(self) -> OpCode: ...
    @property
    def output(self) -> Optional[Varnode]: ...

class Translation:
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def ops(self) -> List[PcodeOp]: ...

class Context:
    def __init__(self, *args, **kwargs) -> None: ...
    def disassemble(
        self,
        bytes: bytes,
        base_address: int = ...,
        offset: int = ...,
        max_bytes: int = ...,
        max_instructions: int = ...,
    ) -> Disassembly: ...
    def getAllRegisters(self) -> dict[Varnode, str]: ...
    def getRegisterName(self, space: AddrSpace, offset: int, size: int) -> str: ...
    def reset(self) -> None: ...
    def setVariableDefault(self, name: str, value: int) -> None: ...
    def translate(
        self,
        bytes: bytes,
        base_address: int = ...,
        offset: int = ...,
        max_bytes: int = ...,
        max_instructions: int = ...,
        flags: int = ...,
    ) -> Translation: ...
