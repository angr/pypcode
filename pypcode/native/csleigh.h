/*
 * Minimal SLEIGH library C API, for disassembly and translation to P-code.
 */
#ifndef CSLEIGH_H
#define CSLEIGH_H

#include <stdbool.h>

#include "sleigh/types.h"

/* Names in this header are prefixed to avoid collisions with SLEIGH. */
#define LPX(name) csleigh_ ## name

#ifdef __cplusplus
extern "C" {
#endif

#define OPS_X \
	INV_OP( 0, INVALID,           "Invalid") \
	DEC_OP( 1, COPY,              "Copy one operand to another") \
	DEC_OP( 2, LOAD,              "Load from a pointer into a specified address space") \
	DEC_OP( 3, STORE,             "Store at a pointer into a specified address space") \
	DEC_OP( 4, BRANCH,            "Always branch") \
	DEC_OP( 5, CBRANCH,           "Conditional branch") \
	DEC_OP( 6, BRANCHIND,         "Indirect branch (jumptable)") \
	DEC_OP( 7, CALL,              "Call to an absolute address") \
	DEC_OP( 8, CALLIND,           "Call through an indirect address") \
	DEC_OP( 9, CALLOTHER,         "User-defined operation") \
	DEC_OP(10, RETURN,            "Return from subroutine") \
	DEC_OP(11, INT_EQUAL,         "Integer comparison, equality (==)") \
	DEC_OP(12, INT_NOTEQUAL,      "Integer comparison, in-equality (!=)") \
	DEC_OP(13, INT_SLESS,         "Integer comparison, signed less-than (<)") \
	DEC_OP(14, INT_SLESSEQUAL,    "Integer comparison, signed less-than-or-equal (<=)") \
	DEC_OP(15, INT_LESS,          "Integer comparison, unsigned less-than (<)") \
	DEC_OP(16, INT_LESSEQUAL,     "Integer comparison, unsigned less-than-or-equal (<=)") \
	DEC_OP(17, INT_ZEXT,          "Zero extension") \
	DEC_OP(18, INT_SEXT,          "Sign extension") \
	DEC_OP(19, INT_ADD,           "Addition, signed or unsigned (+)") \
	DEC_OP(20, INT_SUB,           "Subtraction, signed or unsigned (-)") \
	DEC_OP(21, INT_CARRY,         "Test for unsigned carry") \
	DEC_OP(22, INT_SCARRY,        "Test for signed carry") \
	DEC_OP(23, INT_SBORROW,       "Test for signed borrow") \
	DEC_OP(24, INT_2COMP,         "Twos complement") \
	DEC_OP(25, INT_NEGATE,        "Logical/bitwise negation (~)") \
	DEC_OP(26, INT_XOR,           "Logical/bitwise exclusive-or (^)") \
	DEC_OP(27, INT_AND,           "Logical/bitwise and (&)") \
	DEC_OP(28, INT_OR,            "Logical/bitwise or (|)") \
	DEC_OP(29, INT_LEFT,          "Left shift (<<)") \
	DEC_OP(30, INT_RIGHT,         "Right shift, logical (>>)") \
	DEC_OP(31, INT_SRIGHT,        "Right shift, arithmetic (>>)") \
	DEC_OP(32, INT_MULT,          "Integer multiplication, signed and unsigned (*)") \
	DEC_OP(33, INT_DIV,           "Integer division, unsigned (/)") \
	DEC_OP(34, INT_SDIV,          "Integer division, signed (/)") \
	DEC_OP(35, INT_REM,           "Remainder/modulo, unsigned (%)") \
	DEC_OP(36, INT_SREM,          "Remainder/modulo, signed (%)") \
	DEC_OP(37, BOOL_NEGATE,       "Boolean negate (!)") \
	DEC_OP(38, BOOL_XOR,          "Boolean exclusive-or (^^)") \
	DEC_OP(39, BOOL_AND,          "Boolean and (&&)") \
	DEC_OP(40, BOOL_OR,           "Boolean or (||)") \
	DEC_OP(41, FLOAT_EQUAL,       "Floating-point comparison, equality (==)") \
	DEC_OP(42, FLOAT_NOTEQUAL,    "Floating-point comparison, in-equality (!=)") \
	DEC_OP(43, FLOAT_LESS,        "Floating-point comparison, less-than (<)") \
	DEC_OP(44, FLOAT_LESSEQUAL,   "Floating-point comparison, less-than-or-equal (<=)") \
	INV_OP(45, INVALID,           "Invalid") \
	DEC_OP(46, FLOAT_NAN,         "Not-a-number test (NaN)") \
	DEC_OP(47, FLOAT_ADD,         "Floating-point addition (+)") \
	DEC_OP(48, FLOAT_DIV,         "Floating-point division (/)") \
	DEC_OP(49, FLOAT_MULT,        "Floating-point multiplication (*)") \
	DEC_OP(50, FLOAT_SUB,         "Floating-point subtraction (-)") \
	DEC_OP(51, FLOAT_NEG,         "Floating-point negation (-)") \
	DEC_OP(52, FLOAT_ABS,         "Floating-point absolute value (abs)") \
	DEC_OP(53, FLOAT_SQRT,        "Floating-point square root (sqrt)") \
	DEC_OP(54, FLOAT_INT2FLOAT,   "Convert an integer to a floating-point") \
	DEC_OP(55, FLOAT_FLOAT2FLOAT, "Convert between different floating-point sizes") \
	DEC_OP(56, FLOAT_TRUNC,       "Round towards zero") \
	DEC_OP(57, FLOAT_CEIL,        "Round towards +infinity") \
	DEC_OP(58, FLOAT_FLOOR,       "Round towards -infinity") \
	DEC_OP(59, FLOAT_ROUND,       "Round towards nearest") \
	DEC_OP(60, MULTIEQUAL,        "Phi-node operator") \
	DEC_OP(61, INDIRECT,          "Copy with an indirect effect") \
	DEC_OP(62, PIECE,             "Concatenate") \
	DEC_OP(63, SUBPIECE,          "Truncate") \
	DEC_OP(64, CAST,              "Cast from one data-type to another") \
	DEC_OP(65, PTRADD,            "Index into an array ([])") \
	DEC_OP(66, PTRSUB,            "Drill down to a sub-field  (->)") \
	DEC_OP(67, SEGMENTOP,         "Look-up a segmented address") \
	DEC_OP(68, CPOOLREF,          "Recover a value from the constant pool") \
	DEC_OP(69, NEW,               "Allocate a new object (new)") \
	DEC_OP(70, INSERT,            "Insert a bit-range") \
	DEC_OP(71, EXTRACT,           "Extract a bit-range") \
	DEC_OP(72, POPCOUNT,          "Count the 1-bits") \

#define OP(opname) LPX(CPUI_ ## opname)

typedef enum {
#define DEC_OP(oid, oname, odesc) OP(oname) = oid,
#define INV_OP(oid, oname, odesc)
OPS_X
#undef DEC_OP
#undef INV_OP
} LPX(OpCode);

/* Opaque types */
typedef void *LPX(Context);
typedef void *LPX(AddrSpace);

typedef struct {
	LPX(AddrSpace) space;
	uintb          offset;
} LPX(Address);

typedef struct {
	LPX(AddrSpace) space;
	uintb          offset;
	uint4          size;
} LPX(Varnode);

typedef struct {
	LPX(Address) pc;
	uintm        uniq;
	uintm        order;
} LPX(SeqNum);

typedef struct {
	LPX(SeqNum)   seq;
	LPX(OpCode)   opcode;
	LPX(Varnode) *output; /* NULL if no output */
	LPX(Varnode) *inputs;
	unsigned int  inputs_count;
} LPX(PcodeOp);

typedef enum {
	LPX(ERROR_TYPE_NOERROR) = 0,
	LPX(ERROR_TYPE_GENERIC) = 1,
	LPX(ERROR_TYPE_UNIMPL)  = 2,
	LPX(ERROR_TYPE_BADDATA) = 3,
} LPX(ErrorType);

typedef struct {
	LPX(Address) address;
	int4 instruction_length;
} LPX(UnimplError);

typedef struct {
	LPX(Address) address;
} LPX(BadDataError);

typedef struct {
	LPX(ErrorType)  type;
	const char     *explain;
	union {
		LPX(UnimplError)  unimpl;
		LPX(BadDataError) baddata;
	};
} LPX(Error);

typedef struct {
	LPX(Address)  address;
	int4          length;
	const char   *asm_mnem;
	const char   *asm_body;
	LPX(PcodeOp) *ops;
	unsigned int  ops_count;
} LPX(Translation);

typedef struct {
	LPX(Error)        error;
	LPX(Translation) *instructions;
	unsigned int      instructions_count;
} LPX(TranslationResult);

/*
 * Create a translation context
 */
LPX(Context) LPX(createContext)(const char *slafile);

/*
 * Free a translation context
 */
void LPX(destroyContext)(LPX(Context) c);

/*
 * Translate machine code to P-code
 */
LPX(TranslationResult) *LPX(translate)(LPX(Context) c, const unsigned char *bytes, unsigned int num_bytes, uintb address, unsigned int max_instructions, bool bb_terminating);

/*
 * Free a TranslationResult
 */
void LPX(freeResult)(LPX(TranslationResult) *r);

/*
 * ContextDatabase::setVariableDefault
 */
void LPX(setVariableDefault)(LPX(Context) c, const char *name, uintm val);

/*
 * Address::isConstant
 */
int LPX(Addr_isConstant)(LPX(Address) *a);

/*
 * Address::getSpaceFromConst
 */
LPX(AddrSpace) LPX(Addr_getSpaceFromConst)(LPX(Address) *a);

/*
 * AddrSpace::getName
 */
const char *LPX(AddrSpace_getName)(LPX(AddrSpace) as);

/*
 * Sleigh::getRegisterName
 */
const char *LPX(Sleigh_getRegisterName)(LPX(Context) c, LPX(AddrSpace) as, uintb off, int4 size);

#ifdef __cplusplus
} /* extern "C" { */
#endif

#endif
