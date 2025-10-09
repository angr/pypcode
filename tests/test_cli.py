#!/usr/bin/env python3
# pylint:disable=no-self-use

import unittest
import base64
import tempfile
import sys
import os
import io
from unittest import mock

from pypcode.__main__ import main


def run_cli(*args):
    with mock.patch("sys.argv", [sys.executable, *args]), mock.patch("sys.stdout", new=io.StringIO()) as fake_out:
        try:
            main()
        except SystemExit:
            pass
        return fake_out.getvalue()


class TestCli(unittest.TestCase):
    """
    Test the pypcode module command line interface
    """

    def test_language_list(self):
        output = run_cli("-l")
        assert "x86:LE:64:default" in output

    def test_language_suggestions(self):
        output = run_cli("x86", "_")
        assert 'Language "x86" not found.' in output
        assert "Suggestions:" in output
        assert "x86:LE:32:default" in output
        assert "x86:LE:64:default" in output

    def test_language_no_suggestions(self):
        output = run_cli("xyz", "_")
        assert "Suggestions:" not in output

    def test_translate(self):
        with tempfile.NamedTemporaryFile(delete=False) as tf:
            tf.write(base64.b64decode("McA5xnYRSInBg+EfigwKMAwHSP/A6+vD"))
            tf.close()
            path = tf.name

        try:
            output = run_cli("x86:LE:64:default", path)
            assert "0x17/1: RET" in output
        finally:
            os.unlink(path)

    def test_failed_translation(self):
        with tempfile.NamedTemporaryFile(delete=False) as tf:
            tf.write(b"\x40\x40")
            tf.close()
            path = tf.name

        try:
            output = run_cli("x86:LE:64:default", path)
            assert "An error occurred" in output
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
