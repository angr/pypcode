#!/usr/bin/env python3
import json
import os
from pathlib import Path
import platform
import shutil
import struct
import subprocess
import sys

from setuptools import setup
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
        cross_compiling_for_emscripten = os.getenv("_PYTHON_HOST_PLATFORM", "").startswith("emscripten")
        cross_compiling = (
            cross_compiling_for_macos_arm64 or cross_compiling_for_macos_amd64 or cross_compiling_for_emscripten
        )

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
        if cross_compiling_for_emscripten:
            import nanobind  # pylint: disable=import-error,import-outside-toplevel

            pywasmcross_args = json.loads(os.environ["PYWASMCROSS_ARGS"])
            target_cmake_config_args += [
                f"-DPython_INCLUDE_DIR={pywasmcross_args['pythoninclude']}",
                f"-Dnanobind_DIR={nanobind.cmake_dir()}",
                "-DPYPCODE_BUILD_SLEIGH=OFF",
            ]
        if cross_compiling_for_macos_arm64 or cross_compiling_for_macos_amd64:
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
            host_cmake_config_args = ["-DPYPCODE_BUILD_EXTENSION=OFF"]
            host_cmake = "cmake"
            host_env = None
            if cross_compiling_for_emscripten:
                wrapper_dir = os.environ["COMPILER_WRAPPER_DIR"]
                host_path = os.pathsep.join(
                    path for path in os.environ["PATH"].split(os.pathsep) if path != wrapper_dir
                )
                host_cmake = shutil.which("cmake", path=host_path)
                if host_cmake is None:
                    raise RuntimeError("Could not find the host CMake executable")
                host_env = os.environ.copy()
                host_env["PATH"] = host_path
                for name in (
                    "AR",
                    "CC",
                    "CFLAGS",
                    "CMAKE_CROSSCOMPILING_EMULATOR",
                    "CMAKE_TOOLCHAIN_FILE",
                    "CXX",
                    "CXXFLAGS",
                    "LD",
                    "LDFLAGS",
                    "RANLIB",
                ):
                    host_env.pop(name, None)
            subprocess.check_call(
                [host_cmake, "-S", ".", "-B", host_build_dir] + host_cmake_config_args,
                cwd=root_dir,
                env=host_env,
            )
            subprocess.check_call(
                [host_cmake, "--build", host_build_dir, "--parallel", "--verbose", "--target", "sleigh"]
                + cmake_build_args,
                cwd=root_dir,
                env=host_env,
            )

        # Install extension and sleigh binary into target package
        if cross_compiling:
            # Note: Manually install because cmake install step may refuse to install binaries for foreign architectures
            ext_path = next(target_build_dir.glob("pypcode_native.*"))
            if not cross_compiling_for_emscripten:
                install_pkg_bin_dir.mkdir(exist_ok=True)
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
    package_data={
        "pypcode": add_pkg_data_dirs("pypcode", ["bin", "docs", "processors"]) + ["py.typed", "pypcode_native.pyi"]
    },
    cmdclass={"build_ext": BuildExtension},
)
