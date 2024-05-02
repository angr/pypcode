#!/usr/bin/env python3
import os
from pathlib import Path
import platform
import shutil
import struct
import subprocess
import sys
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


class BuildExtension(build_ext):
    """
    Runs cmake to build the pypcode_native extension, sleigh binary, and runs sleigh to build .sla files.
    """

    def run(self):
        try:
            subprocess.check_output(["cmake", "--version"])
        except OSError as exc:
            raise RuntimeError("Please install CMake to build") from exc

        cross_compiling_for_macos_arm64 = (
            platform.system() == "Darwin" and platform.machine() == "x86_64" and "arm64" in os.getenv("ARCHFLAGS", "")
        )
        cross_compiling_for_macos_amd64 = (
            platform.system() == "Darwin" and platform.machine() != "x86_64" and "x86_64" in os.getenv("ARCHFLAGS", "")
        )
        cross_compiling = cross_compiling_for_macos_arm64 or cross_compiling_for_macos_amd64

        root_dir = Path(__file__).parent.absolute()
        target_build_dir = root_dir / "build" / "native"
        host_build_dir = target_build_dir / "host"
        install_pkg_root_dir = (root_dir if self.inplace else Path(self.build_lib).absolute()) / "pypcode"
        install_pkg_bin_dir = install_pkg_root_dir / "bin"
        host_bin_root_dir = host_build_dir if cross_compiling else install_pkg_bin_dir
        sleigh_filename = "sleigh" + (".exe" if platform.system() == "Windows" else "")
        sleigh_bin = host_bin_root_dir / sleigh_filename
        specfiles_dir = install_pkg_root_dir / "processors"

        # Build sleigh and pypcode_native extension
        cmake_config_args = [
            f"-DCMAKE_INSTALL_PREFIX={install_pkg_root_dir}",
            f"-DPython_EXECUTABLE={sys.executable}",
        ]
        cmake_build_args = []
        if platform.system() == "Windows":
            is_64b = struct.calcsize("P") * 8 == 64
            cmake_config_args += ["-A", "x64" if is_64b else "Win32"]
            cmake_build_args += ["--config", "Release"]

        target_cmake_config_args = cmake_config_args[::]
        if cross_compiling:
            target_cmake_config_args += [
                "-DCMAKE_OSX_DEPLOYMENT_TARGET=10.14",
                "-DCMAKE_OSX_ARCHITECTURES=" + os.getenv("ARCHFLAGS"),
            ]
        subprocess.check_call(["cmake", "-S", ".", "-B", target_build_dir] + target_cmake_config_args, cwd=root_dir)
        subprocess.check_call(
            ["cmake", "--build", target_build_dir, "--parallel", "--verbose"] + cmake_build_args,
            cwd=root_dir,
        )

        if cross_compiling:
            # Also build a host version of sleigh to process .sla files
            host_cmake_config_args = cmake_config_args
            subprocess.check_call(["cmake", "-S", ".", "-B", host_build_dir] + host_cmake_config_args, cwd=root_dir)
            subprocess.check_call(
                ["cmake", "--build", host_build_dir, "--parallel", "--verbose", "--target", "sleigh"]
                + cmake_build_args,
                cwd=root_dir,
            )

        # Install extension and sleigh binary into target package
        if cross_compiling:
            # Note: Manually install because cmake install step may refuse to install binaries for foreign architectures
            install_pkg_bin_dir.mkdir(exist_ok=True)
            ext_path = next(target_build_dir.glob("pypcode_native.*"))
            shutil.copy(target_build_dir / sleigh_filename, install_pkg_bin_dir / sleigh_filename)
            shutil.copy(ext_path, install_pkg_root_dir / ext_path.name)
        else:
            subprocess.check_call(["cmake", "--install", target_build_dir], cwd=root_dir)

        # Build sla files
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
