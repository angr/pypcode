#!/usr/bin/env python3
import os
import platform
import struct
import subprocess
import sys
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
LIB_SRC_DIR = os.path.join(ROOT_DIR, "pypcode", "native")


class BuildExtension(build_ext):
    """
    Runs cmake to build the pypcode_native extension, sleigh binary, and runs sleigh to build .sla files.
    """

    def run(self):
        try:
            subprocess.check_output(["cmake", "--version"])
        except OSError as exc:
            raise RuntimeError("Please install CMake to build") from exc

        install_pkg_root = os.path.abspath(os.path.join(ROOT_DIR if self.inplace else self.build_lib, "pypcode"))
        cmake_install_prefix = install_pkg_root
        cmake_config_args = [
            f"-DCMAKE_INSTALL_PREFIX={cmake_install_prefix}",
            f"-DPython_EXECUTABLE={sys.executable}",
        ]
        cmake_build_args = []
        if platform.system() == "Windows":
            is_64b = struct.calcsize("P") * 8 == 64
            cmake_config_args += ["-A", "x64" if is_64b else "Win32"]
            cmake_build_args += ["--config", "Release"]

        # Build sleigh and pypcode_native extension
        subprocess.check_call(["cmake", "-S", ".", "-B", "build"] + cmake_config_args, cwd=LIB_SRC_DIR)
        subprocess.check_call(
            ["cmake", "--build", "build", "--parallel", "--verbose"] + cmake_build_args,
            cwd=LIB_SRC_DIR,
        )
        subprocess.check_call(["cmake", "--install", "build"], cwd=LIB_SRC_DIR)

        # Build sla files
        bin_ext = ".exe" if platform.system() == "Windows" else ""
        sleigh_bin = os.path.join(install_pkg_root, "bin", "sleigh" + bin_ext)
        specfiles_dir = os.path.join(install_pkg_root, "processors")
        subprocess.check_call([sleigh_bin, "-a", specfiles_dir])


def add_pkg_data_dirs(pkg, dirs):
    pkg_data = []
    for d in dirs:
        for root, _, files in os.walk(os.path.join(pkg, d)):
            r = os.path.relpath(root, pkg)
            pkg_data.extend([os.path.join(r, f) for f in files])
    return pkg_data


setup(
    ext_modules=[Extension(name="pypcode_native", sources=[])],
    package_data={
        "pypcode": add_pkg_data_dirs("pypcode", ["bin", "docs", "processors"]) + ["py.typed", "pypcode_native.pyi"]
    },
    cmdclass={"build_ext": BuildExtension},
)
