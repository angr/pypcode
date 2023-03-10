from typing import Any, Optional, Sequence, TypeAlias

import _cffi_backend

CData: TypeAlias = _cffi_backend._CDataBase
charp: TypeAlias = CData

csleigh_CPUI_BOOL_AND: int
csleigh_CPUI_BOOL_NEGATE: int
csleigh_CPUI_BOOL_OR: int
csleigh_CPUI_BOOL_XOR: int
csleigh_CPUI_BRANCH: int
csleigh_CPUI_BRANCHIND: int
csleigh_CPUI_CALL: int
csleigh_CPUI_CALLIND: int
csleigh_CPUI_CALLOTHER: int
csleigh_CPUI_CAST: int
csleigh_CPUI_CBRANCH: int
csleigh_CPUI_COPY: int
csleigh_CPUI_CPOOLREF: int
csleigh_CPUI_EXTRACT: int
csleigh_CPUI_FLOAT_ABS: int
csleigh_CPUI_FLOAT_ADD: int
csleigh_CPUI_FLOAT_CEIL: int
csleigh_CPUI_FLOAT_DIV: int
csleigh_CPUI_FLOAT_EQUAL: int
csleigh_CPUI_FLOAT_FLOAT2FLOAT: int
csleigh_CPUI_FLOAT_FLOOR: int
csleigh_CPUI_FLOAT_INT2FLOAT: int
csleigh_CPUI_FLOAT_LESS: int
csleigh_CPUI_FLOAT_LESSEQUAL: int
csleigh_CPUI_FLOAT_MULT: int
csleigh_CPUI_FLOAT_NAN: int
csleigh_CPUI_FLOAT_NEG: int
csleigh_CPUI_FLOAT_NOTEQUAL: int
csleigh_CPUI_FLOAT_ROUND: int
csleigh_CPUI_FLOAT_SQRT: int
csleigh_CPUI_FLOAT_SUB: int
csleigh_CPUI_FLOAT_TRUNC: int
csleigh_CPUI_INDIRECT: int
csleigh_CPUI_INSERT: int
csleigh_CPUI_INT_2COMP: int
csleigh_CPUI_INT_ADD: int
csleigh_CPUI_INT_AND: int
csleigh_CPUI_INT_CARRY: int
csleigh_CPUI_INT_DIV: int
csleigh_CPUI_INT_EQUAL: int
csleigh_CPUI_INT_LEFT: int
csleigh_CPUI_INT_LESS: int
csleigh_CPUI_INT_LESSEQUAL: int
csleigh_CPUI_INT_MULT: int
csleigh_CPUI_INT_NEGATE: int
csleigh_CPUI_INT_NOTEQUAL: int
csleigh_CPUI_INT_OR: int
csleigh_CPUI_INT_REM: int
csleigh_CPUI_INT_RIGHT: int
csleigh_CPUI_INT_SBORROW: int
csleigh_CPUI_INT_SCARRY: int
csleigh_CPUI_INT_SDIV: int
csleigh_CPUI_INT_SEXT: int
csleigh_CPUI_INT_SLESS: int
csleigh_CPUI_INT_SLESSEQUAL: int
csleigh_CPUI_INT_SREM: int
csleigh_CPUI_INT_SRIGHT: int
csleigh_CPUI_INT_SUB: int
csleigh_CPUI_INT_XOR: int
csleigh_CPUI_INT_ZEXT: int
csleigh_CPUI_LOAD: int
csleigh_CPUI_MULTIEQUAL: int
csleigh_CPUI_NEW: int
csleigh_CPUI_PIECE: int
csleigh_CPUI_POPCOUNT: int
csleigh_CPUI_PTRADD: int
csleigh_CPUI_PTRSUB: int
csleigh_CPUI_RETURN: int
csleigh_CPUI_SEGMENTOP: int
csleigh_CPUI_STORE: int
csleigh_CPUI_SUBPIECE: int
csleigh_ERROR_TYPE_BADDATA: int
csleigh_ERROR_TYPE_GENERIC: int
csleigh_ERROR_TYPE_NOERROR: int
csleigh_ERROR_TYPE_UNIMPL: int

def csleigh_AddrSpace_getName(*args, **kwargs) -> Any: ...
def csleigh_Addr_getSpaceFromConst(*args, **kwargs) -> Any: ...
def csleigh_Addr_isConstant(*args, **kwargs) -> Any: ...
def csleigh_Sleigh_getAllRegisters(*args, **kwargs) -> Any: ...
def csleigh_Sleigh_getRegisterName(*args, **kwargs) -> Any: ...
def csleigh_createContext(*args, **kwargs) -> Any: ...
def csleigh_destroyContext(*args, **kwargs) -> Any: ...
def csleigh_freeResult(*args, **kwargs) -> Any: ...
def csleigh_setVariableDefault(*args, **kwargs) -> Any: ...
def csleigh_translate(*args, **kwargs) -> Any: ...

csleigh_OpCode: TypeAlias = int
csleigh_ErrorType: TypeAlias = int

class csleigh_Context:
    pass

class csleigh_AddrSpace:
    pass

class csleigh_Address:
    offset: int
    space: csleigh_AddrSpace

class csleigh_Varnode:
    space: csleigh_AddrSpace
    offset: int
    size: int

class csleigh_SeqNum:
    pc: csleigh_Address
    uniq: int
    order: int

class csleigh_PcodeOp:
    seq: csleigh_SeqNum
    opcode: csleigh_OpCode
    output: Optional[csleigh_Varnode]
    inputs: Sequence[csleigh_Varnode]
    inputs_count: int

class csleigh_UnimplError:
    address: csleigh_Address
    instruction_length: int

class csleigh_BadDataError:
    address: csleigh_Address

class csleigh_Error:
    type: csleigh_ErrorType
    explain: charp
    unimpl: csleigh_UnimplError
    baddata: csleigh_BadDataError

class csleigh_Translation:
    address: csleigh_Address
    length: int
    asm_mnem: charp
    asm_body: charp
    ops: Sequence[csleigh_PcodeOp]
    ops_count: int

class csleigh_TranslationResult:
    error: csleigh_Error
    instructions: Sequence[csleigh_Translation]
    instructions_count: int

class csleigh_RegisterDefinition:
    name: charp
    varnode: csleigh_Varnode
