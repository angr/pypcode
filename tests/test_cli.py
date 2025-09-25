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
        main()
        return fake_out.getvalue()


class TestCli(unittest.TestCase):
    """
    Test the pypcode module command line interface
    """

    def test_cli_list(self):
        output = run_cli("-l")
        assert "x86:LE:64:default" in output

    def test_cli_trans(self):
        with tempfile.NamedTemporaryFile(delete=False) as tf:
            tf.write(base64.b64decode("McA5xnYRSInBg+EfigwKMAwHSP/A6+vD"))
            tf.close()
            path = tf.name

        try:
            output = run_cli("x86:LE:64:default", path)
            assert "0x17/1: RET" in output
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
