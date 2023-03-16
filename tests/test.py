#!/usr/bin/env python3
# pylint:disable=no-self-use

from unittest import main, TestCase

from pypcode import ArchLanguage, BadDataError, Context, ContextCreationError, UnimplError


class Tests(TestCase):
    """
    Basic tests
    """

    def test_failed_context_creation(self):
        lang = ArchLanguage.from_id("x86:LE:64:default")
        bad_lang = ArchLanguage("/bad/arch/path", lang.ldef)
        with self.assertRaises(ContextCreationError):
            Context(bad_lang)

    def test_x86_64_translation(self):
        ctx = Context(ArchLanguage.from_id("x86:LE:64:default"))
        result = ctx.translate(b"\x48\x35\x78\x56\x34\x12\xc3", 0)
        assert len(result.instructions) == 2

    def test_decode_failure(self):
        ctx = Context(ArchLanguage.from_id("x86:LE:64:default"))
        with self.assertRaises(BadDataError):
            ctx.translate(b"\x40\x40", 0)

    def test_unimpl_failure(self):
        ctx = Context(ArchLanguage.from_id("Toy:BE:32:default"))
        with self.assertRaises(UnimplError):
            ctx.translate(b"\xa8\x00", 0)


if __name__ == "__main__":
    main()
