#!/usr/bin/env python3
# pylint:disable=no-self-use

import gc
import logging
import subprocess
import sys
import textwrap
from pathlib import Path
from typing import cast
from unittest import TestCase, main
from unittest.mock import create_autospec

from pypcode import (
    AddrSpace,
    Arch,
    ArchLanguage,
    BadDataError,
    Context,
    LowlevelError,
    OpCode,
    PcodeOp,
    TranslateFlags,
    Translation,
    UnimplError,
    Varnode,
)
from pypcode.printing import OpFormat, PcodePrettyPrinter

# logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def get_imarks(translation: Translation) -> list[PcodeOp]:
    return [op for op in translation.ops if op.opcode == OpCode.IMARK]


def varnode_location(varnode: Varnode) -> tuple[str, int, int]:
    return varnode.space.name, varnode.offset, varnode.size


def unique_definitions(translation: Translation) -> dict[tuple[str, int, int], PcodeOp]:
    return {
        varnode_location(op.output): op
        for op in translation.ops
        if op.output is not None and op.output.space.name == "unique"
    }


def unique_definition(varnode: Varnode, definitions: dict[tuple[str, int, int], PcodeOp]) -> PcodeOp | None:
    definition = definitions.get(varnode_location(varnode))
    if definition is not None or varnode.space.name != "unique":
        return definition
    return next(
        (
            candidate
            for (space, offset, size), candidate in definitions.items()
            if space == "unique" and offset == varnode.offset and size >= varnode.size
        ),
        None,
    )


def dependency_ops(varnode: Varnode, definitions: dict[tuple[str, int, int], PcodeOp]) -> list[PcodeOp]:
    definition = unique_definition(varnode, definitions)
    if definition is None:
        return []
    return [definition, *(nested for value in definition.inputs for nested in dependency_ops(value, definitions))]


def dependency_registers(varnode: Varnode, definitions: dict[tuple[str, int, int], PcodeOp]) -> set[str]:
    if varnode.space.name == "register":
        return {varnode.getRegisterName()}
    definition = unique_definition(varnode, definitions)
    if definition is None:
        return set()
    return {name for value in definition.inputs for name in dependency_registers(value, definitions)}


def relative_memory_offset(varnode: Varnode, definitions: dict[tuple[str, int, int], PcodeOp]) -> int:
    definition = unique_definition(varnode, definitions)
    if definition is None or definition.opcode != OpCode.INT_ADD:
        return 0

    constants = [value for value in definition.inputs if value.space.name == "const"]
    nonconstants = [value for value in definition.inputs if value.space.name != "const"]
    if len(constants) != 1 or len(nonconstants) != 1:
        return 0
    return constants[0].offset + relative_memory_offset(nonconstants[0], definitions)


def memory_access_layout(translation: Translation, opcode: OpCode) -> list[tuple[int, int]]:
    definitions = unique_definitions(translation)
    accesses = []
    for op in translation.ops:
        if op.opcode != opcode:
            continue
        if opcode == OpCode.LOAD:
            assert op.output is not None
            width = op.output.size
        else:
            width = op.inputs[2].size
        accesses.append((relative_memory_offset(op.inputs[1], definitions), width))
    return sorted(accesses)


def memory_access_at(translation: Translation, opcode: OpCode, offset: int) -> PcodeOp:
    definitions = unique_definitions(translation)
    return next(
        op
        for op in translation.ops
        if op.opcode == opcode and relative_memory_offset(op.inputs[1], definitions) == offset
    )


def register_write(translation: Translation, register: str) -> PcodeOp:
    return next(
        op for op in reversed(translation.ops) if op.output is not None and op.output.getRegisterName() == register
    )


class ContextTests(TestCase):
    """
    Basic Context tests
    """

    def tearDown(self):
        gc.collect()

    def test_bad_context_language_type(self):
        with self.assertRaises(TypeError):
            Context(1234)

    def test_can_create_all_language_contexts(self):
        for arch in Arch.enumerate():
            for lang in arch.languages:
                with self.subTest(lang=lang.id):
                    log.debug("Creating context for %s", lang.id)
                    Context(lang)

    def test_context_creation_failure(self):
        lang = ArchLanguage.from_id("x86:LE:64:default")
        bad_lang = ArchLanguage("/bad/arch/path", lang.ldef)
        with self.assertRaises(LowlevelError):
            Context(bad_lang)

    def test_context_premature_release(self):
        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\xc3")
        del ctx
        log.debug("Should not crash: %d", len(tx.ops[0].inputs[0].space.name))
        del tx
        log.debug("--")

        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\xc3")
        op = tx.ops[0]
        del tx  # Should not be released
        del ctx  # Should not be released while op is alive
        log.debug("Should not crash: %d", len(op.inputs[0].space.name))
        del op  # Now ctx, tx can be released
        log.debug("--")

        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\xc3")
        vn = tx.ops[0].inputs[0]
        del tx
        del ctx
        log.debug("Should not crash: %d", len(vn.space.name))
        del vn  # Now ctx, tx can be released
        log.debug("--")

        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\xc3")
        space = tx.ops[0].inputs[0].space
        del tx
        del ctx
        log.debug("Should not crash: %d", len(space.name))
        del space  # Now ctx, tx can be released. Space is managed by context, so C++ obj should not be released.
        log.debug("--")

    def test_reset_preserves_retained_result_address_spaces(self):
        script = textwrap.dedent("""
            from pypcode import Context, OpCode

            ctx = Context("x86:LE:16:Real Mode")
            translation = ctx.translate(b"\\x31\\xc0\\xc3")
            operation = next(op for op in translation.ops if op.opcode == OpCode.INT_XOR)
            varnode = operation.inputs[0]
            space = varnode.space
            disassembly = ctx.disassemble(b"\\x90\\xc3")
            instruction = disassembly.instructions[0]
            address = instruction.addr

            for _ in range(64):
                ctx.reset()
                assert ctx.translate(b"\\x90\\xc3").ops
                assert ctx.disassemble(b"\\x90\\xc3").instructions
                assert varnode.getRegisterName() == "AX"
                assert space.name == "register"
                assert address.space.name == "ram"
                assert instruction.addr.offset == 0
            """)
        result = subprocess.run(
            [sys.executable, "-c", script],
            capture_output=True,
            check=False,
            cwd=Path(sys.modules[Context.__module__].__file__).parent.parent,
            text=True,
        )
        assert result.returncode == 0, result.stderr


class RegistersTests(TestCase):
    """
    Context register lookup tests
    """

    def test_registers(self):
        ctx = Context("x86:LE:64:default")
        assert "RAX" in ctx.registers

    def test_registers_retain_native_context_state(self):
        script = textwrap.dedent("""
            import gc

            from pypcode import Context

            cached_context = Context("x86:LE:16:Real Mode")
            cached_register = cached_context.registers["AX"]
            cached_context.reset()
            del cached_context

            direct_context = Context("x86:LE:16:Real Mode")
            all_registers = direct_context.getAllRegisters()
            direct_register = next(varnode for varnode, name in all_registers.items() if name == "BX")
            del all_registers, direct_context

            space_context = Context("x86:LE:16:Real Mode")
            register_space = space_context.registers["CX"].space
            del space_context
            gc.collect()

            for _ in range(64):
                assert cached_register.getRegisterName() == "AX"
                assert cached_register.space.name == "register"
                assert register_space.name == "register"
                assert direct_register.getRegisterName() == "BX"
                assert direct_register.space.name == "register"

            del cached_register, direct_register, register_space
            gc.collect()
            """)
        result = subprocess.run(
            [sys.executable, "-c", script],
            capture_output=True,
            check=False,
            cwd=Path(sys.modules[Context.__module__].__file__).parent.parent,
            text=True,
        )
        assert result.returncode == 0, result.stderr
        assert "nanobind: leaked" not in result.stderr

    def test_getRegisterName(self):
        ctx = Context("x86:LE:64:default")
        ri = ctx.registers["RAX"]
        assert ctx.getRegisterName(ri.space, ri.offset, ri.size) == "RAX"


class AddrSpaceTests(TestCase):
    """
    AddrSpace tests
    """

    def test_name(self):
        ctx = Context("x86:LE:64:default")
        assert ctx.translate(b"\xeb\xfe").ops[1].inputs[0].space.name == "ram"


class VarnodeTests(TestCase):
    """
    Varnode tests
    """

    def test_getSpaceFromConst(self):
        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\x48\x8b\x41\x01")  # mov rax, [rcx + 1]
        assert tx.ops[2].inputs[0].getSpaceFromConst().name == "ram"

    def test_getRegisterName(self):
        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\x48\x8b\x41\x01")  # mov rax, [rcx + 1]
        assert tx.ops[1].inputs[0].getRegisterName() == "RCX"
        assert tx.ops[1].inputs[1].getRegisterName() == ""

    def test_getUserDefinedOpName(self):
        ctx = Context("AARCH64:LE:64:AppleSilicon")
        ctx.setVariableDefault("ShowPAC", 1)
        ctx.setVariableDefault("PAC_clobber", 1)

        tx = ctx.translate(b"\x7f\x23\x03\xd5")  # pacibsp

        # x30 = pacib(x30, sp)
        assert tx.ops[1].opcode == OpCode.CALLOTHER
        assert tx.ops[1].output.getRegisterName() == "x30"
        assert tx.ops[1].inputs[0].getUserDefinedOpName() == "pacib"
        assert tx.ops[1].inputs[1].getRegisterName() == "x30"
        assert tx.ops[1].inputs[2].getRegisterName() == "sp"


class DisassembleTests(TestCase):
    """
    Context::disassemble tests
    """

    def test_disassemble(self):
        ctx = Context("x86:LE:64:default")
        dx = ctx.disassemble(b"\x90\xeb\xfe")
        assert len(dx.instructions) == 2
        ins = dx.instructions[1]
        assert ins.addr.offset == 1
        assert ins.length == 2
        assert ins.mnem == "JMP"
        assert ins.body == "0x1"

    def test_decode_failure(self):
        ctx = Context("x86:LE:64:default")
        with self.assertRaises(BadDataError):
            ctx.disassemble(b"\x40\x40")

    def test_truncated_instruction(self):
        ctx = Context("x86:LE:16:Real Mode")
        with self.assertRaises(BadDataError):
            ctx.disassemble(b"\xe8")
        with self.assertRaises(BadDataError):
            ctx.disassemble(b"\xe8\x00\x00", max_bytes=1)
        with self.assertRaises(BadDataError):
            ctx.disassemble(b"\x90\xe8", offset=1)

        dx = ctx.disassemble(b"\x90")
        assert len(dx.instructions) == 1
        assert dx.instructions[0].mnem == "NOP"

        dx = ctx.disassemble(b"\x90\xe8")
        assert len(dx.instructions) == 1
        assert dx.instructions[0].mnem == "NOP"

        dx = ctx.disassemble(b"\xe8\x00\x00")
        assert len(dx.instructions) == 1
        assert dx.instructions[0].length == 3
        assert dx.instructions[0].mnem == "CALL"

        ctx = Context("MIPS:BE:32:default")
        dx = ctx.disassemble(b"\x10@\x00\x06")
        assert len(dx.instructions) == 1
        assert dx.instructions[0].length == 4

    def test_partial_decode_failure(self):
        ctx = Context("x86:LE:64:default")
        dx = ctx.disassemble(b"\xff\xc0\x90\x40\x40")  # inc eax; nop; bad
        assert len(dx.instructions) == 2

    def test_not_cached(self):
        ctx = Context("x86:LE:64:default")
        dx = ctx.disassemble(b"\xeb\xfe", 5)
        dx = ctx.disassemble(b"\xc3", 5)
        ins = dx.instructions[0]
        assert ins.addr.offset == 5
        assert ins.length == 1
        assert ins.mnem == "RET"
        assert ins.body == ""

    def test_arg_base_address(self):
        ctx = Context("x86:LE:64:default")
        dx = ctx.disassemble(b"\xeb\xfe", 10)
        assert len(dx.instructions) == 1
        assert dx.instructions[0].mnem == "JMP"
        assert dx.instructions[0].body == "0xa"

    def test_arg_offset(self):
        ctx = Context("x86:LE:64:default")
        dx = ctx.disassemble(b"\x90\xeb\xfe", offset=1)
        assert len(dx.instructions) == 1

    def test_arg_offset_out_of_range(self):
        ctx = Context("x86:LE:64:default")
        with self.assertRaises(IndexError):
            ctx.disassemble(b"\x90\xeb\xfe", offset=3)

    def test_arg_max_bytes(self):
        ctx = Context("x86:LE:64:default")
        dx = ctx.disassemble(b"\x90\xeb\xfe", max_bytes=1)
        assert len(dx.instructions) == 1

    def test_arg_max_instructions(self):
        ctx = Context("x86:LE:64:default")
        dx = ctx.disassemble(b"\x90\xeb\xfe", max_instructions=1)
        assert len(dx.instructions) == 1

    def test_pretty_printing(self):
        ctx = Context("x86:LE:64:default")
        dx = ctx.disassemble(b"\x48\x31\xc0\xc3")
        assert "0x0/3: XOR RAX,RAX" in str(dx)
        assert "0x3/1: RET" in str(dx)


class TranslateTests(TestCase):
    """
    Context::translate tests
    """

    def test_translate(self):
        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\x48\x35\x78\x56\x34\x12\xc3")
        assert len(get_imarks(tx)) == 2

    def test_x86_indirect_far_jump_loads_segment_and_offset(self):
        for language, instruction, offset_size in (
            ("x86:LE:16:Protected Mode", b"\xff\x2e\xe6\x08", 2),
            ("x86:LE:16:Real Mode", b"\xff\x2e\xe6\x08", 2),
            ("x86:LE:32:default", b"\xff\x2d\xe6\x08\x00\x00", 4),
        ):
            with self.subTest(language=language):
                tx = Context(language).translate(instruction)
                loads = [op for op in tx.ops if op.opcode == OpCode.LOAD]
                segment = [
                    op
                    for op in tx.ops
                    if op.opcode == OpCode.CALLOTHER and op.inputs[0].getUserDefinedOpName() == "segment"
                ][-1]
                branch = next(op for op in tx.ops if op.opcode == OpCode.BRANCHIND)

                assert [op.output.size for op in loads] == [2, offset_size]
                assert any(op.opcode == OpCode.INT_ADD and op.inputs[1].offset == offset_size for op in tx.ops)
                assert varnode_location(segment.inputs[1]) == varnode_location(loads[0].output)
                assert varnode_location(segment.inputs[2]) == varnode_location(loads[1].output)
                assert varnode_location(branch.inputs[0]) == varnode_location(segment.output)

    def test_x86_16bit_far_indirect_control_flow_uses_effective_segment(self):
        cases = (
            ("SS override", "SS", b"\x36\xff\x1e\x34\x12", b"\x36\xff\x2e\x34\x12"),
            ("ES override", "ES", b"\x26\xff\x1e\x34\x12", b"\x26\xff\x2e\x34\x12"),
            ("BP default", "SS", b"\xff\x5e\x10", b"\xff\x6e\x10"),
            ("BX default", "DS", b"\xff\x1f", b"\xff\x2f"),
            ("DI default", "DS", b"\xff\x1d", b"\xff\x2d"),
        )
        for language in ("x86:LE:16:Protected Mode", "x86:LE:16:Real Mode"):
            for operation, control_opcode in (
                ("CALLF", OpCode.CALLIND),
                ("JMPF", OpCode.BRANCHIND),
            ):
                for addressing, expected_segment, call_instruction, jump_instruction in cases:
                    instruction = call_instruction if operation == "CALLF" else jump_instruction
                    with self.subTest(
                        language=language,
                        operation=operation,
                        addressing=addressing,
                    ):
                        tx = Context(language).translate(instruction, max_instructions=1)
                        segments = [
                            op
                            for op in tx.ops
                            if op.opcode == OpCode.CALLOTHER and op.inputs[0].getUserDefinedOpName() == "segment"
                        ]
                        loads = [op for op in tx.ops if op.opcode == OpCode.LOAD]
                        control = next(op for op in tx.ops if op.opcode == control_opcode)

                        assert segments[0].inputs[1].getRegisterName() == expected_segment
                        assert [op.output.size for op in loads] == [2, 2]
                        assert any(
                            varnode_location(load.inputs[1]) == varnode_location(segments[0].output) for load in loads
                        )
                        assert varnode_location(control.inputs[0]) == varnode_location(segments[1].output)

    def test_x86_16bit_operand_override_far_call_loads_16_32_pointer(self):
        for language in ("x86:LE:16:Protected Mode", "x86:LE:16:Real Mode"):
            with self.subTest(language=language):
                tx = Context(language).translate(b"\x66\xff\x1f", max_instructions=1)  # callf m16:32 [bx]
                loads = [op for op in tx.ops if op.opcode == OpCode.LOAD]
                stores = [op for op in tx.ops if op.opcode == OpCode.STORE]
                segments = [
                    op
                    for op in tx.ops
                    if op.opcode == OpCode.CALLOTHER and op.inputs[0].getUserDefinedOpName() == "segment"
                ]
                call = next(op for op in tx.ops if op.opcode == OpCode.CALLIND)
                target_segment = next(
                    op for op in segments if varnode_location(op.output) == varnode_location(call.inputs[0])
                )

                assert [op.output.size for op in loads] == [2, 4]
                assert [op.inputs[2].size for op in stores] == [2, 4]
                assert any(op.opcode == OpCode.INT_ADD and op.inputs[1].offset == 4 for op in tx.ops)
                assert varnode_location(target_segment.inputs[1]) == varnode_location(loads[0].output)
                assert varnode_location(target_segment.inputs[2]) == varnode_location(loads[1].output)

    def test_x86_16bit_operand_override_near_jump_uses_eax_and_current_cs(self):
        for language in ("x86:LE:16:Protected Mode", "x86:LE:16:Real Mode"):
            with self.subTest(language=language):
                tx = Context(language).translate(b"\x66\xff\xe0", max_instructions=1)  # jmp eax
                segment = [
                    op
                    for op in tx.ops
                    if op.opcode == OpCode.CALLOTHER and op.inputs[0].getUserDefinedOpName() == "segment"
                ][-1]
                branch = next(op for op in tx.ops if op.opcode == OpCode.BRANCHIND)

                assert segment.inputs[1].getRegisterName() == "CS"
                assert segment.inputs[2].getRegisterName() == "EAX"
                assert varnode_location(branch.inputs[0]) == varnode_location(segment.output)

    def test_x86_16bit_operand_override_near_call_uses_eax_and_current_cs(self):
        for language in ("x86:LE:16:Protected Mode", "x86:LE:16:Real Mode"):
            with self.subTest(language=language):
                tx = Context(language).translate(b"\x66\xff\xd0", max_instructions=1)  # call eax
                call = next(op for op in tx.ops if op.opcode == OpCode.CALLIND)
                segment = next(
                    op
                    for op in tx.ops
                    if op.opcode == OpCode.CALLOTHER
                    and op.inputs[0].getUserDefinedOpName() == "segment"
                    and varnode_location(op.output) == varnode_location(call.inputs[0])
                )
                stores = [op for op in tx.ops if op.opcode == OpCode.STORE]

                assert segment.inputs[1].getRegisterName() == "CS"
                assert segment.inputs[2].getRegisterName() == "EAX"
                assert [op.inputs[2].size for op in stores] == [4]

    def test_x86_16bit_xlat_uses_segment_override(self):
        for language in ("x86:LE:16:Protected Mode", "x86:LE:16:Real Mode"):
            with self.subTest(language=language):
                tx = Context(language).translate(b"\x26\xd7")  # xlat es:[bx]
                segment = next(
                    op
                    for op in tx.ops
                    if op.opcode == OpCode.CALLOTHER and op.inputs[0].getUserDefinedOpName() == "segment"
                )
                load = next(op for op in tx.ops if op.opcode == OpCode.LOAD)

                assert segment.inputs[1].getRegisterName() == "ES"
                assert any(
                    op.opcode == OpCode.INT_ADD
                    and op.inputs[0].getRegisterName() == "BX"
                    and op.inputs[1].size == 2
                    and varnode_location(op.output) == varnode_location(segment.inputs[2])
                    for op in tx.ops
                )
                assert varnode_location(load.inputs[1]) == varnode_location(segment.output)

    def test_x86_x87_environment_store_layouts_and_exception_masking(self):
        env16 = sorted((offset, 2) for offset in range(0, 14, 2))
        env32_protected = sorted(((0, 2), (4, 2), (8, 2), (12, 4), (16, 2), (18, 2), (20, 4), (24, 2)))
        env32_real = sorted(((0, 2), (4, 2), (8, 2), (12, 2), (16, 4), (20, 2), (24, 4)))
        cases = (
            (
                "16-bit protected",
                "x86:LE:16:Protected Mode",
                (bytes.fromhex("d976e6"), bytes.fromhex("9bd976e6")),
                env16,
            ),
            (
                "16-bit real",
                "x86:LE:16:Real Mode",
                (bytes.fromhex("d937"), bytes.fromhex("9bd937")),
                env16,
            ),
            (
                "32-bit protected",
                "x86:LE:32:default",
                (bytes.fromhex("d930"), bytes.fromhex("9bd930")),
                env32_protected,
            ),
            (
                "32-bit real",
                "x86:LE:16:Real Mode",
                (bytes.fromhex("66d937"), bytes.fromhex("669bd937")),
                env32_real,
            ),
        )

        for mode, language, instructions, expected_layout in cases:
            for instruction in instructions:
                with self.subTest(mode=mode, instruction=instruction.hex()):
                    translation = Context(language).translate(instruction, max_instructions=1)
                    assert memory_access_layout(translation, OpCode.STORE) == expected_layout

                    control_write = register_write(translation, "FPUControlWord")
                    assert control_write.opcode == OpCode.INT_OR
                    assert any(value.space.name == "const" and value.offset == 0x3F for value in control_write.inputs)
                    assert translation.ops.index(control_write) > max(
                        index for index, op in enumerate(translation.ops) if op.opcode == OpCode.STORE
                    )

    def test_x86_x87_environment_load_layouts(self):
        env16 = sorted((offset, 2) for offset in range(0, 14, 2))
        cases = (
            ("16-bit protected", "x86:LE:16:Protected Mode", bytes.fromhex("d966e6"), env16),
            ("16-bit real", "x86:LE:16:Real Mode", bytes.fromhex("d927"), env16),
            (
                "32-bit protected",
                "x86:LE:32:default",
                bytes.fromhex("d920"),
                sorted(((0, 2), (4, 2), (8, 2), (12, 4), (16, 2), (18, 2), (20, 4), (24, 2))),
            ),
            (
                "32-bit real",
                "x86:LE:16:Real Mode",
                bytes.fromhex("66d927"),
                sorted(((0, 2), (4, 2), (8, 2), (12, 2), (16, 4), (20, 2), (24, 4))),
            ),
        )

        for mode, language, instruction, expected_layout in cases:
            with self.subTest(mode=mode):
                translation = Context(language).translate(instruction, max_instructions=1)
                assert memory_access_layout(translation, OpCode.LOAD) == expected_layout

                definitions = unique_definitions(translation)
                status_write = register_write(translation, "FPUStatusWord")
                assert status_write.opcode == OpCode.LOAD
                assert relative_memory_offset(status_write.inputs[1], definitions) == (2 if "16-bit" in mode else 4)
                for register, shift in {"C0": None, "C1": 9, "C2": 10, "C3": 14}.items():
                    write = register_write(translation, register)
                    dependencies = [write, *dependency_ops(write.inputs[0], definitions)]
                    assert dependency_registers(write.inputs[0], definitions) == {"FPUStatusWord"}
                    assert any(
                        op.opcode == OpCode.INT_AND
                        and any(value.space.name == "const" and value.offset == 1 for value in op.inputs)
                        for op in dependencies
                    )
                    if shift is None:
                        assert any(
                            op.opcode == OpCode.SUBPIECE
                            and op.inputs[0].getRegisterName() == "FPUStatusWord"
                            and op.inputs[1].offset == 1
                            for op in dependencies
                        )
                    else:
                        assert any(
                            op.opcode == OpCode.INT_RIGHT
                            and any(value.space.name == "const" and value.offset == shift for value in op.inputs)
                            for op in dependencies
                        )

    def test_x86_x87_state_save_restore_uses_operand_sized_register_start(self):
        env16 = sorted((offset, 2) for offset in range(0, 14, 2))
        env32_protected = sorted(((0, 2), (4, 2), (8, 2), (12, 4), (16, 2), (18, 2), (20, 4), (24, 2)))
        env32_real = sorted(((0, 2), (4, 2), (8, 2), (12, 2), (16, 4), (20, 2), (24, 4)))
        cases = (
            (
                "16-bit protected",
                "x86:LE:16:Protected Mode",
                (bytes.fromhex("dd76e6"), bytes.fromhex("9bdd76e6")),
                bytes.fromhex("dd66e6"),
                env16,
                14,
                94,
            ),
            (
                "16-bit real",
                "x86:LE:16:Real Mode",
                (bytes.fromhex("dd37"), bytes.fromhex("9bdd37")),
                bytes.fromhex("dd27"),
                env16,
                14,
                94,
            ),
            (
                "32-bit protected",
                "x86:LE:32:default",
                (bytes.fromhex("dd30"), bytes.fromhex("9bdd30")),
                bytes.fromhex("dd20"),
                env32_protected,
                28,
                108,
            ),
            (
                "32-bit real",
                "x86:LE:16:Real Mode",
                (bytes.fromhex("66dd37"), bytes.fromhex("669bdd37")),
                bytes.fromhex("66dd27"),
                env32_real,
                28,
                108,
            ),
            (
                "64-bit protected",
                "x86:LE:64:default",
                (bytes.fromhex("dd30"), bytes.fromhex("9bdd30")),
                bytes.fromhex("dd20"),
                env32_protected,
                28,
                108,
            ),
        )

        for mode, language, save_instructions, restore_instruction, env_layout, stack_start, image_size in cases:
            expected_layout = sorted((*env_layout, *((stack_start + index * 10, 10) for index in range(8))))
            for instruction in save_instructions:
                with self.subTest(mode=mode, operation="save", instruction=instruction.hex()):
                    translation = Context(language).translate(instruction, max_instructions=1)
                    layout = memory_access_layout(translation, OpCode.STORE)
                    assert layout == expected_layout
                    assert max(offset + width for offset, width in layout) == image_size

                    last_store = max(index for index, op in enumerate(translation.ops) if op.opcode == OpCode.STORE)
                    reset_values = {
                        "FPUControlWord": 0x037F,
                        "FPUStatusWord": 0,
                        "FPUTagWord": 0xFFFF,
                        "FPUDataPointer": 0,
                        "FPUInstructionPointer": 0,
                        "FPULastInstructionOpcode": 0,
                        "FPUPointerSelector": 0,
                        "FPUDataSelector": 0,
                        "C0": 0,
                        "C1": 0,
                        "C2": 0,
                        "C3": 0,
                    }
                    for register, expected_value in reset_values.items():
                        write = register_write(translation, register)
                        assert write.opcode == OpCode.COPY
                        assert write.inputs[0].space.name == "const"
                        assert write.inputs[0].offset == expected_value
                        assert translation.ops.index(write) > last_store

            with self.subTest(mode=mode, operation="restore"):
                translation = Context(language).translate(restore_instruction, max_instructions=1)
                layout = memory_access_layout(translation, OpCode.LOAD)
                assert layout == expected_layout
                assert max(offset + width for offset, width in layout) == image_size

    def test_x86_x87_environment_protected_selectors_and_real_pointer_packing(self):
        protected16_store = Context("x86:LE:16:Protected Mode").translate(bytes.fromhex("d976e6"))
        protected16_load = Context("x86:LE:16:Protected Mode").translate(bytes.fromhex("d966e6"))
        real16_store = Context("x86:LE:16:Real Mode").translate(bytes.fromhex("d937"))
        real16_load = Context("x86:LE:16:Real Mode").translate(bytes.fromhex("d927"))
        definitions = unique_definitions(protected16_store)

        assert dependency_registers(memory_access_at(protected16_store, OpCode.STORE, 6).inputs[2], definitions) == {
            "FPUInstructionPointer"
        }
        assert dependency_registers(memory_access_at(protected16_store, OpCode.STORE, 8).inputs[2], definitions) == {
            "FPUPointerSelector"
        }
        assert dependency_registers(memory_access_at(protected16_store, OpCode.STORE, 10).inputs[2], definitions) == {
            "FPUDataPointer"
        }
        assert dependency_registers(memory_access_at(protected16_store, OpCode.STORE, 12).inputs[2], definitions) == {
            "FPUDataSelector"
        }
        assert (12, 4) not in memory_access_layout(protected16_store, OpCode.STORE)

        definitions = unique_definitions(protected16_load)
        assert {
            relative_memory_offset(op.inputs[1], definitions)
            for op in dependency_ops(register_write(protected16_load, "FPUInstructionPointer").inputs[0], definitions)
            if op.opcode == OpCode.LOAD
        } == {6}
        pointer_selector_write = register_write(protected16_load, "FPUPointerSelector")
        pointer_selector_dependencies = [
            pointer_selector_write,
            *(nested for value in pointer_selector_write.inputs for nested in dependency_ops(value, definitions)),
        ]
        assert {
            relative_memory_offset(op.inputs[1], definitions)
            for op in pointer_selector_dependencies
            if op.opcode == OpCode.LOAD
        } == {8}

        definitions = unique_definitions(real16_store)
        instruction_pack = memory_access_at(real16_store, OpCode.STORE, 8).inputs[2]
        data_pack = memory_access_at(real16_store, OpCode.STORE, 12).inputs[2]
        assert dependency_registers(instruction_pack, definitions) == {
            "FPUInstructionPointer",
            "FPULastInstructionOpcode",
        }
        assert dependency_registers(data_pack, definitions) == {"FPUDataPointer"}
        instruction_constants = {
            value.offset
            for op in dependency_ops(instruction_pack, definitions)
            for value in op.inputs
            if value.space.name == "const"
        }
        assert {4, 0x7FF, 0xF000} <= instruction_constants

        definitions = unique_definitions(real16_load)
        expected_loads = {
            "FPUInstructionPointer": {6, 8},
            "FPULastInstructionOpcode": {8},
            "FPUDataPointer": {10, 12},
        }
        for register, expected_offsets in expected_loads.items():
            write = register_write(real16_load, register)
            dependencies = [write, *(nested for value in write.inputs for nested in dependency_ops(value, definitions))]
            assert {
                relative_memory_offset(op.inputs[1], definitions) for op in dependencies if op.opcode == OpCode.LOAD
            } == expected_offsets

        protected32_store = Context("x86:LE:32:default").translate(bytes.fromhex("d930"))
        protected32_load = Context("x86:LE:32:default").translate(bytes.fromhex("d920"))
        definitions = unique_definitions(protected32_store)
        expected_registers = {
            12: {"FPUInstructionPointer"},
            16: {"FPUPointerSelector"},
            18: {"FPULastInstructionOpcode"},
            20: {"FPUDataPointer"},
            24: {"FPUDataSelector"},
        }
        for offset, expected in expected_registers.items():
            value = memory_access_at(protected32_store, OpCode.STORE, offset).inputs[2]
            assert dependency_registers(value, definitions) == expected

        definitions = unique_definitions(protected32_load)
        expected_loads = {
            "FPUInstructionPointer": {12},
            "FPUPointerSelector": {16},
            "FPULastInstructionOpcode": {18},
            "FPUDataPointer": {20},
            "FPUDataSelector": {24},
        }
        for register, expected_offsets in expected_loads.items():
            write = register_write(protected32_load, register)
            dependencies = [write, *(nested for value in write.inputs for nested in dependency_ops(value, definitions))]
            assert {
                relative_memory_offset(op.inputs[1], definitions) for op in dependencies if op.opcode == OpCode.LOAD
            } == expected_offsets

        real32_store = Context("x86:LE:16:Real Mode").translate(bytes.fromhex("66d937"))
        real32_load = Context("x86:LE:16:Real Mode").translate(bytes.fromhex("66d927"))
        definitions = unique_definitions(real32_store)
        instruction_pack = memory_access_at(real32_store, OpCode.STORE, 16).inputs[2]
        data_pack = memory_access_at(real32_store, OpCode.STORE, 24).inputs[2]
        assert dependency_registers(instruction_pack, definitions) == {
            "FPUInstructionPointer",
            "FPULastInstructionOpcode",
        }
        assert dependency_registers(data_pack, definitions) == {"FPUDataPointer"}
        instruction_constants = {
            value.offset
            for op in dependency_ops(instruction_pack, definitions)
            for value in op.inputs
            if value.space.name == "const"
        }
        assert {4, 0x7FF, 0x0FFFF000} <= instruction_constants

        definitions = unique_definitions(real32_load)
        expected_loads = {
            "FPUInstructionPointer": {12, 16},
            "FPULastInstructionOpcode": {16},
            "FPUDataPointer": {20, 24},
        }
        for register, expected_offsets in expected_loads.items():
            write = register_write(real32_load, register)
            dependencies = [write, *(nested for value in write.inputs for nested in dependency_ops(value, definitions))]
            assert {
                relative_memory_offset(op.inputs[1], definitions) for op in dependencies if op.opcode == OpCode.LOAD
            } == expected_offsets

    def test_x86_x87_operand_override_selects_reciprocal_environment_format(self):
        cases = (
            ("x86:LE:16:Protected Mode", bytes.fromhex("d937"), bytes.fromhex("66d937"), 14, 26),
            ("x86:LE:16:Real Mode", bytes.fromhex("d937"), bytes.fromhex("66d937"), 14, 28),
            ("x86:LE:32:default", bytes.fromhex("d930"), bytes.fromhex("66d930"), 26, 14),
        )
        for language, default_instruction, override_instruction, default_extent, override_extent in cases:
            with self.subTest(language=language):
                default_layout = memory_access_layout(
                    Context(language).translate(default_instruction, max_instructions=1), OpCode.STORE
                )
                override_layout = memory_access_layout(
                    Context(language).translate(override_instruction, max_instructions=1), OpCode.STORE
                )
                assert max(offset + width for offset, width in default_layout) == default_extent
                assert max(offset + width for offset, width in override_layout) == override_extent

    def test_x86_x87_64bit_languages_use_protected_environment_format(self):
        expected_layout = sorted(((0, 2), (4, 2), (8, 2), (12, 4), (16, 2), (18, 2), (20, 4), (24, 2)))
        expected_registers = {
            12: {"FPUInstructionPointer"},
            16: {"FPUPointerSelector"},
            18: {"FPULastInstructionOpcode"},
            20: {"FPUDataPointer"},
            24: {"FPUDataSelector"},
        }
        for language in ("x86:LE:64:default", "x86:LE:64:compat32"):
            with self.subTest(language=language, operation="store"):
                translation = Context(language).translate(bytes.fromhex("d930"), max_instructions=1)
                assert memory_access_layout(translation, OpCode.STORE) == expected_layout
                definitions = unique_definitions(translation)
                for offset, expected in expected_registers.items():
                    value = memory_access_at(translation, OpCode.STORE, offset).inputs[2]
                    assert dependency_registers(value, definitions) == expected

            with self.subTest(language=language, operation="load"):
                translation = Context(language).translate(bytes.fromhex("d920"), max_instructions=1)
                assert memory_access_layout(translation, OpCode.LOAD) == expected_layout
                definitions = unique_definitions(translation)
                for offset, expected in expected_registers.items():
                    register = next(iter(expected))
                    write = register_write(translation, register)
                    dependencies = [
                        write,
                        *(nested for value in write.inputs for nested in dependency_ops(value, definitions)),
                    ]
                    assert {
                        relative_memory_offset(op.inputs[1], definitions)
                        for op in dependencies
                        if op.opcode == OpCode.LOAD
                    } == {offset}

            with self.subTest(language=language, operation="store-16"):
                translation = Context(language).translate(bytes.fromhex("66d930"), max_instructions=1)
                assert memory_access_layout(translation, OpCode.STORE) == [(offset, 2) for offset in range(0, 14, 2)]
                definitions = unique_definitions(translation)
                assert dependency_registers(memory_access_at(translation, OpCode.STORE, 8).inputs[2], definitions) == {
                    "FPUPointerSelector"
                }
                assert dependency_registers(memory_access_at(translation, OpCode.STORE, 12).inputs[2], definitions) == {
                    "FPUDataSelector"
                }

            with self.subTest(language=language, operation="load-16"):
                translation = Context(language).translate(bytes.fromhex("66d920"), max_instructions=1)
                definitions = unique_definitions(translation)
                for register, offset in (("FPUPointerSelector", 8), ("FPUDataSelector", 12)):
                    write = register_write(translation, register)
                    assert write.opcode == OpCode.LOAD
                    assert relative_memory_offset(write.inputs[1], definitions) == offset

    def test_decode_failure(self):
        ctx = Context("x86:LE:64:default")
        with self.assertRaises(BadDataError):
            ctx.translate(b"\x40\x40")

    def test_truncated_instruction(self):
        ctx = Context("x86:LE:16:Real Mode")
        with self.assertRaises(BadDataError):
            ctx.translate(b"\xe8")
        with self.assertRaises(BadDataError):
            ctx.translate(b"\xe8\x00\x00", max_bytes=1)
        with self.assertRaises(BadDataError):
            ctx.translate(b"\x90\xe8", offset=1)

        tx = ctx.translate(b"\x90")
        imarks = get_imarks(tx)
        assert len(imarks) == 1
        assert imarks[0].inputs[0].size == 1

        tx = ctx.translate(b"\x90\xe8")
        imarks = get_imarks(tx)
        assert len(imarks) == 1
        assert imarks[0].inputs[0].size == 1

        tx = ctx.translate(b"\xe8\x00\x00")
        imarks = get_imarks(tx)
        assert len(imarks) == 1
        assert imarks[0].inputs[0].size == 3

    def test_truncated_unimplemented_instruction(self):
        ctx = Context("Toy:BE:32:default")
        with self.assertRaises(BadDataError):
            ctx.translate(b"\xa8")
        with self.assertRaises(UnimplError):
            ctx.translate(b"\xa8\x00")

    def test_truncated_delay_slot(self):
        ctx = Context("MIPS:BE:32:default")
        with self.assertRaises(BadDataError):
            ctx.translate(b"\x10@\x00\x06")
        with self.assertRaises(BadDataError):
            ctx.translate(b"\x10@\x00\x06\x00 \x08%", max_bytes=4)

    def test_truncated_inst_next2(self):
        ctx = Context("Toy:BE:32:builder")
        for buf in (bytes.fromhex("8000d9"), bytes.fromhex("8000d932")):
            with self.subTest(buf=buf), self.assertRaises(BadDataError):
                ctx.translate(buf, max_instructions=1)
        with self.assertRaises(BadDataError):
            ctx.translate(bytes.fromhex("8000d9320000"), max_bytes=4, max_instructions=1)

        tx = ctx.translate(bytes.fromhex("8000d9320000"), max_instructions=1)
        branch = next(op for op in tx.ops if op.opcode == OpCode.CBRANCH)
        assert branch.inputs[0].offset == 6

    def test_inst_next2_not_cached(self):
        ctx = Context("Toy:BE:32:builder")
        tx = ctx.translate(bytes.fromhex("80000000"), max_instructions=1)
        branch = next(op for op in tx.ops if op.opcode == OpCode.CBRANCH)
        assert branch.inputs[0].offset == 4

        tx = ctx.translate(bytes.fromhex("8000d9320000"), max_instructions=1)
        branch = next(op for op in tx.ops if op.opcode == OpCode.CBRANCH)
        assert branch.inputs[0].offset == 6

    def test_partial_decode_failure(self):
        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\xff\xc0\x40\x40")  # inc eax; bad
        assert len(get_imarks(tx)) == 1

    def test_unimpl_failure(self):
        ctx = Context("Toy:BE:32:default")
        with self.assertRaises(UnimplError):
            ctx.translate(b"\xa8\x00")

    def test_partial_unimpl_failure(self):
        ctx = Context("Toy:BE:32:default")
        tx = ctx.translate(b"\xd0\x00\xa8\x00")  # and r0, r0; unimpl
        assert len(get_imarks(tx)) == 1

    def test_not_cached(self):
        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\xeb\xfe", 5)
        tx = ctx.translate(b"\xc3", 5)
        assert tx.ops[-1].opcode == OpCode.RETURN

    def test_translate_and_disassemble_not_cached(self):
        ctx = Context("x86:LE:64:default")
        dx = ctx.disassemble(b"\xeb\xfe", 5)
        tx = ctx.translate(b"\xc3", 5)
        assert tx.ops[-1].opcode == OpCode.RETURN

        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\xc3", 5)
        dx = ctx.disassemble(b"\xeb\xfe", 5)
        assert len(dx.instructions) == 1
        ins = dx.instructions[0]
        assert ins.addr.offset == 5
        assert ins.length == 2
        assert ins.mnem == "JMP"
        assert ins.body == "0x5"

    def test_arg_base_address(self):
        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\xeb\xfe", 10)  # jmp $
        assert len(tx.ops) == 2
        assert len(tx.ops[0].inputs) == 1  # Check just one instruction decoded
        assert tx.ops[0].inputs[0].offset == 10  # Check IMARK
        assert tx.ops[1].inputs[0].offset == 10  # Check jump target

    def test_arg_offset(self):
        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\x90\x90\xeb\xfe", offset=2)  # nop; nop; jmp $
        assert len(get_imarks(tx)) == 1

    def test_arg_offset_out_of_range(self):
        ctx = Context("x86:LE:64:default")
        with self.assertRaises(IndexError):
            ctx.translate(b"\x90\x90\xeb\xfe", offset=10)  # nop; nop; jmp $

    def test_arg_max_bytes(self):
        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\x90\x90\x90", max_bytes=1)
        assert len(get_imarks(tx)) == 1

    def test_arg_max_instructions(self):
        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\x90\x90\x90", max_instructions=2)
        assert len(get_imarks(tx)) == 2

    def test_arg_flag_bb_terminating(self):
        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\x90\xeb\xfe\x90\x90", flags=TranslateFlags.BB_TERMINATING)
        assert len(get_imarks(tx)) == 2

    def test_delay_slot(self):
        ctx = Context("MIPS:BE:32:default")
        tx = ctx.translate(b"\x10@\x00\x06\x00 \x08%", 0x4009F4)
        imarks = get_imarks(tx)
        assert len(imarks) == 1
        assert len(imarks[0].inputs) == 2
        assert imarks[0].inputs[0].offset == 0x4009F4
        assert imarks[0].inputs[0].size == 4
        assert imarks[0].inputs[1].offset == 0x4009F8
        assert imarks[0].inputs[1].size == 4

    def test_variable_length_delay_slot(self):
        ctx = Context("Toy:BE:32:builder")
        tx = ctx.translate(bytes.fromhex("f500d9320000d000"), max_instructions=3)
        assert [[(vn.offset, vn.size) for vn in imark.inputs] for imark in get_imarks(tx)] == [
            [(0, 2), (2, 4)],
            [(6, 2)],
        ]

    def test_pretty_printing(self):
        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\x48\x31\xc0")
        assert "RAX = RAX ^ RAX" in str(tx)


class PrintingTests(TestCase):
    """
    Pretty printing tests.
    """

    def test_branches(self):
        for opc, output in [
            (OpCode.BRANCH, "goto ram[123:4]"),
            (OpCode.BRANCHIND, "goto [ram[123:4]]"),
            (OpCode.CALL, "call ram[123:4]"),
            (OpCode.CALLIND, "call [ram[123:4]]"),
            (OpCode.RETURN, "return ram[123:4]"),
        ]:
            vn = cast(Varnode, create_autospec(Varnode, instance=True, spec_set=True))
            vn.space.name = "ram"
            vn.offset = 0x123
            vn.size = 4

            op = cast(PcodeOp, create_autospec(PcodeOp, instance=True, spec_set=True))
            op.opcode = opc
            op.output = None
            op.inputs = [vn]

            assert PcodePrettyPrinter.fmt_op(op) == output

    def test_cbranch(self):
        target_vn = cast(Varnode, create_autospec(Varnode, instance=True, spec_set=True))
        target_vn.space.name = "ram"
        target_vn.offset = 0x456
        target_vn.size = 4

        cond_vn = cast(Varnode, create_autospec(Varnode, instance=True, spec_set=True))
        cond_vn.space.name = "ram"
        cond_vn.offset = 0x123
        cond_vn.size = 1

        op = cast(PcodeOp, create_autospec(PcodeOp, instance=True, spec_set=True))
        op.opcode = OpCode.CBRANCH
        op.output = None
        op.inputs = [target_vn, cond_vn]

        assert PcodePrettyPrinter.fmt_op(op) == "if (ram[123:1]) goto ram[456:4]"

    def test_load(self):
        dest_vn = cast(Varnode, create_autospec(Varnode, instance=True, spec_set=True))
        dest_vn.space.name = "ram"
        dest_vn.offset = 0x123
        dest_vn.size = 1

        space = cast(AddrSpace, create_autospec(AddrSpace, instance=True, spec_set=True))
        space.name = "ram"

        space_vn = cast(Varnode, create_autospec(Varnode, instance=True, spec_set=True))
        space_vn.space.name = "const"
        space_vn.getSpaceFromConst.return_value = space

        offset_vn = cast(Varnode, create_autospec(Varnode, instance=True, spec_set=True))
        offset_vn.space.name = "const"
        offset_vn.offset = 0x456
        offset_vn.size = 1

        op = cast(PcodeOp, create_autospec(PcodeOp, instance=True, spec_set=True))
        op.opcode = OpCode.LOAD
        op.output = dest_vn
        op.inputs = [space_vn, offset_vn]

        assert PcodePrettyPrinter.fmt_op(op) == "ram[123:1] = *[ram]0x456"

    def test_store(self):
        space = cast(AddrSpace, create_autospec(AddrSpace, instance=True, spec_set=True))
        space.name = "ram"

        space_vn = cast(Varnode, create_autospec(Varnode, instance=True, spec_set=True))
        space_vn.space.name = "const"
        space_vn.getSpaceFromConst.return_value = space

        offset_vn = cast(Varnode, create_autospec(Varnode, instance=True, spec_set=True))
        offset_vn.space.name = "const"
        offset_vn.offset = 0x123
        offset_vn.size = 1

        value_vn = cast(Varnode, create_autospec(Varnode, instance=True, spec_set=True))
        value_vn.space.name = "const"
        value_vn.offset = 0x456
        value_vn.size = 1

        op = cast(PcodeOp, create_autospec(PcodeOp, instance=True, spec_set=True))
        op.opcode = OpCode.STORE
        op.output = None
        op.inputs = [space_vn, offset_vn, value_vn]

        assert PcodePrettyPrinter.fmt_op(op) == "*[ram]0x123 = 0x456"

    def test_callother(self):
        target_vn = cast(Varnode, create_autospec(Varnode, instance=True, spec_set=True))
        target_vn.getUserDefinedOpName.return_value = "udop"

        arg_vn = cast(Varnode, create_autospec(Varnode, instance=True, spec_set=True))
        arg_vn.space.name = "const"
        arg_vn.offset = 0x456
        arg_vn.size = 1

        op = cast(PcodeOp, create_autospec(PcodeOp, instance=True, spec_set=True))
        op.opcode = OpCode.CALLOTHER
        op.output = None
        op.inputs = [target_vn, arg_vn]

        assert PcodePrettyPrinter.fmt_op(op) == "udop(0x456)"

    def test_no_regname(self):
        arg_vn = cast(Varnode, create_autospec(Varnode, instance=True, spec_set=True))
        arg_vn.space.name = "register"
        arg_vn.offset = 0x123
        arg_vn.size = 4
        arg_vn.getRegisterName.return_value = None
        assert OpFormat.fmt_vn(arg_vn) == "register[123:4]"


if __name__ == "__main__":
    main()
