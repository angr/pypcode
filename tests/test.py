#!/usr/bin/env python3
# pylint:disable=no-self-use

from unittest import main, TestCase

from pypcode import ArchLanguage, Context


class Tests(TestCase):
    """
    Basic tests
    """

    def test_x86_64_translation(self):
        lang = ArchLanguage.from_id("x86:LE:64:default")
        ctx = Context(lang)
        result = ctx.translate(b"\x48\x35\x78\x56\x34\x12\xc3", 0)
        assert result.error is None
        assert len(result.instructions) == 2


if __name__ == "__main__":
    main()
