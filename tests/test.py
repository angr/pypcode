#!/usr/bin/env python3
# pylint:disable=no-self-use

import gc
import logging
from unittest import main, TestCase
from typing import List

from pypcode import (
    Arch,
    ArchLanguage,
    BadDataError,
    Context,
    DecoderError,
    OpCode,
    PcodeOp,
    TranslateFlags,
    Translation,
    UnimplError,
)

# logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def get_imarks(translation: Translation) -> List[PcodeOp]:
    return [op for op in translation.ops if op.opcode == OpCode.IMARK]


# from pypcode import PcodePrettyPrinter
# def pp_tx(translation: Translation) -> None:
#     for op in translation.ops:
#         log.debug("%s", PcodePrettyPrinter.fmt_op(op))


# def pp_dx(disassembly) -> None:
#     for ins in disassembly:
#         log.debug("%x/%d: %s %s", ins.addr.offset, ins.length, ins.mnem, ins.body)


class ContextTests(TestCase):
    """
    Basic Context tests
    """

    def tearDown(self):
        gc.collect()

    def test_can_create_all_language_contexts(self):
        for arch in Arch.enumerate():
            for lang in arch.languages:
                with self.subTest(lang=lang.id):
                    log.debug("Creating context for %s", lang.id)
                    Context(lang)

    def test_context_creation_failure(self):
        lang = ArchLanguage.from_id("x86:LE:64:default")
        bad_lang = ArchLanguage("/bad/arch/path", lang.ldef)
        with self.assertRaises(DecoderError):
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


class RegistersTests(TestCase):
    """
    Context register lookup tests
    """

    def test_registers(self):
        ctx = Context("x86:LE:64:default")
        assert "RAX" in ctx.registers

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
        tx = ctx.translate(b"\x48\x8B\x41\x01")  # mov rax, [rcx + 1]
        assert tx.ops[2].inputs[0].getSpaceFromConst().name == "ram"

    def test_getRegisterName(self):
        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\x48\x8B\x41\x01")  # mov rax, [rcx + 1]
        assert tx.ops[1].inputs[0].getRegisterName() == "RCX"
        assert tx.ops[1].inputs[1].getRegisterName() == ""


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


class TranslateTests(TestCase):
    """
    Context::translate tests
    """

    def test_translate(self):
        ctx = Context("x86:LE:64:default")
        tx = ctx.translate(b"\x48\x35\x78\x56\x34\x12\xc3")
        assert len(get_imarks(tx)) == 2

    def test_decode_failure(self):
        ctx = Context("x86:LE:64:default")
        with self.assertRaises(BadDataError):
            ctx.translate(b"\x40\x40")

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


if __name__ == "__main__":
    main()
