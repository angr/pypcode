#!/usr/bin/env python3
import os
import sys
from setuptools import setup

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(ROOT_DIR)

import build_cffi  # pylint:disable=wrong-import-position


def add_pkg_data_dirs(pkg, dirs):
    pkg_data = []
    for d in dirs:
        for root, _, files in os.walk(os.path.join(pkg, d)):
            r = os.path.relpath(root, pkg)
            pkg_data.extend([os.path.join(r, f) for f in files])
    return pkg_data


cmdclass = {"build_ext": build_cffi.FfiPreBuildExtension}

try:
    from wheel.bdist_wheel import bdist_wheel

    class bdist_wheel_abi3(bdist_wheel):
        """
        Helper to generate correct platform tag for stable ABI wheels
        """

        def get_tag(self):
            python, abi, plat = super().get_tag()
            if python.startswith("cp"):
                return "cp38", "abi3", plat
            return python, abi, plat

    cmdclass["bdist_wheel"] = bdist_wheel_abi3
except ImportError:
    pass


setup(
    package_data={
        "pypcode": add_pkg_data_dirs("pypcode", ["_csleigh", "bin", "docs", "processors"])
        + ["py.typed", "_csleigh.pyi"]
    },
    cffi_modules=["build_cffi.py:ffibuilder"],
    cmdclass=cmdclass,
)
