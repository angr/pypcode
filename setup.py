#!/usr/bin/env python3
from glob import glob
import os
import platform
import shutil
import struct
import subprocess
import sys
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
TARGET_BUILD_DIR = os.path.join(ROOT_DIR, "build", "native")
HOST_BUILD_DIR = os.path.join(ROOT_DIR, "build", "native", "host")


class BuildExtension(build_ext):
    """
    Runs cmake to build the pypcode_native extension, sleigh binary, and runs sleigh to build .sla files.
    """

    def run(self):
        try:
            subprocess.check_output(["cmake", "--version"])
        except OSError as exc:
            raise RuntimeError("Please install CMake to build") from exc

        # When building pypcode wheels on GitHub Actions using cibuildwheel, ARCHFLAGS will be set
        CROSS_COMPILING_FOR_MACOS_ARM64 = (
            platform.system() == "Darwin" and platform.machine() == "x86_64" and "arm64" in os.getenv("ARCHFLAGS", "")
        )
        CROSS_COMPILING = CROSS_COMPILING_FOR_MACOS_ARM64

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
        target_cmake_config_args = cmake_config_args[::]
        if CROSS_COMPILING_FOR_MACOS_ARM64:
            target_cmake_config_args += [
                "-DCMAKE_OSX_DEPLOYMENT_TARGET=10.14",
                "-DCMAKE_OSX_ARCHITECTURES=arm64",
            ]
        subprocess.check_call(["cmake", "-S", ".", "-B", TARGET_BUILD_DIR] + target_cmake_config_args, cwd=ROOT_DIR)
        subprocess.check_call(
            ["cmake", "--build", TARGET_BUILD_DIR, "--parallel", "--verbose"] + cmake_build_args,
            cwd=ROOT_DIR,
        )

        if CROSS_COMPILING:
            # Also build a host version of sleigh to process .sla files
            host_cmake_config_args = cmake_config_args[::]
            subprocess.check_call(["cmake", "-S", ".", "-B", HOST_BUILD_DIR] + host_cmake_config_args, cwd=ROOT_DIR)
            subprocess.check_call(
                ["cmake", "--build", HOST_BUILD_DIR, "--parallel", "--verbose", "--target", "sleigh"]
                + cmake_build_args,
                cwd=ROOT_DIR,
            )

        bin_ext = ".exe" if platform.system() == "Windows" else ""
        install_pkg_bin_dir = os.path.join(install_pkg_root, "bin")
        sleigh_filename = "sleigh" + bin_ext

        # Install extension and sleigh binary
        if CROSS_COMPILING:
            os.makedirs(install_pkg_bin_dir, exist_ok=True)
            ext_path = glob(TARGET_BUILD_DIR + "/pypcode_native.*")[0]
            shutil.copy(
                os.path.join(TARGET_BUILD_DIR, sleigh_filename), os.path.join(install_pkg_bin_dir, sleigh_filename)
            )
            shutil.copy(ext_path, os.path.join(install_pkg_root, os.path.basename(ext_path)))
        else:
            subprocess.check_call(["cmake", "--install", TARGET_BUILD_DIR], cwd=ROOT_DIR)

        # Build sla files
        host_bin_root = HOST_BUILD_DIR if CROSS_COMPILING else install_pkg_bin_dir
        sleigh_bin = os.path.join(host_bin_root, sleigh_filename)
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
