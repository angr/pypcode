#!/usr/bin/env python3
import os.path
import struct
import subprocess
import platform

from setuptools.command.build_ext import build_ext


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
LIB_SRC_DIR = os.path.join(ROOT_DIR, "pypcode", "native")
CMAKE_BUILD_DIR = os.path.join(LIB_SRC_DIR, "build")


class FfiPreBuildExtension(build_ext):
    """
    FFI Pre-Build Extension
    """

    def pre_run(self, _, ffi):
        try:
            subprocess.check_output(["cmake", "--version"])
        except OSError as exc:
            raise RuntimeError("Please install CMake to build") from exc

        install_pkg_root = os.path.abspath(os.path.join(ROOT_DIR if self.inplace else self.build_lib, "pypcode"))
        cmake_install_prefix = install_pkg_root
        cmake_config_args = [
            "-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON",
            "-DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE",
            f"-DCMAKE_INSTALL_PREFIX={cmake_install_prefix}",
        ]
        cmake_build_args = []
        if platform.system() == "Windows":
            is_64b = struct.calcsize("P") * 8 == 64
            cmake_config_args += ["-A", "x64" if is_64b else "Win32"]
            cmake_build_args += ["--config", "Release"]

        # Build sleigh and csleigh library
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

        with open(os.path.join(CMAKE_BUILD_DIR, "csleigh.i"), encoding="utf-8") as f:
            ffi.cdef(f.read())


def ffibuilder():
    from cffi import FFI  # pylint:disable=import-outside-toplevel

    ffi = FFI()
    LIBS = {"Darwin": ["c++"], "Linux": ["stdc++"]}.get(platform.system(), [])
    ffi.set_source(
        "pypcode._csleigh",
        """
        #include "build/csleigh.i"
        """,
        libraries=["csleigh"] + LIBS,
        include_dirs=[LIB_SRC_DIR],
        library_dirs=[os.path.join(CMAKE_BUILD_DIR, "lib")],
    )
    return ffi


if __name__ == "__main__":
    ffibuilder().compile(verbose=True)
