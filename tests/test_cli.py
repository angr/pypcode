#!/usr/bin/env python3
# pylint:disable=no-self-use

import unittest
import base64
import subprocess
import tempfile
import sys
import os


class TestCli(unittest.TestCase):
    """
    Test the pypcode module command line interface
    """

    def test_cli_list(self):
        subprocess.run([sys.executable, "-m", "pypcode", "-l"], check=True)

    def test_cli_trans(self):
        with tempfile.NamedTemporaryFile(delete=False) as tf:
            tf.write(base64.b64decode("McA5xnYRSInBg+EfigwKMAwHSP/A6+vD"))
            tf.close()
            path = tf.name

        try:
            subprocess.run(
                [sys.executable, "-m", "pypcode", "x86:LE:64:default", path],
                check=True,
            )
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
