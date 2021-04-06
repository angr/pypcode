#!/usr/bin/env python3
import unittest
import base64
import subprocess
import tempfile
import sys
import os

class TestCli(unittest.TestCase):
    def test_cli_list(self):
        subprocess.run([sys.executable, '-m', 'pypcode', '-l'], check=True)

    def test_cli_trans(self):
        tf = tempfile.NamedTemporaryFile(delete=False)
        tf.write(base64.b64decode('McA5xnYRSInBg+EfigwKMAwHSP/A6+vD'))
        tf.close()
        try:
            subprocess.run([sys.executable, '-m', 'pypcode', 'x86:LE:64:default', tf.name], check=True)
        finally:
            os.unlink(tf.name)

if __name__ == '__main__':
    unittest.main()
