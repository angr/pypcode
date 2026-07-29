#!/usr/bin/env python3
import os
import platform
import shutil
import struct
import subprocess
import sys
from pathlib import Path

from setuptools import setup
from setuptools.command.build_ext import build_ext
from setuptools.command.build_py import build_py

_GENERATED_PACKAGE_SUFFIXES = frozenset({".pyc", ".pyd", ".pyo", ".sla", ".so"})


def is_generated_package_path(path):
    path = Path(path)
    return "__pycache__" in path.parts or path.suffix.casefold() in _GENERATED_PACKAGE_SUFFIXES


def ignore_generated_package_entries(directory, names):
    return [name for name in names if is_generated_package_path(Path(directory) / name)]


def stage_processor_sources(source, destination):
    """Replace a staged processor tree with current, non-generated sources."""
    source = Path(source)
    destination = Path(destination)
    if destination.is_symlink() or destination.is_file():
        destination.unlink()
    elif destination.exists():
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, ignore=ignore_generated_package_entries)


def is_strict_editable(command):
    if not command.editable_mode:
        return False
    editable_wheel = command.distribution.get_command_obj("editable_wheel")
    mode = getattr(editable_wheel, "mode", None)
    mode = getattr(mode, "value", mode)
    return isinstance(mode, str) and mode.casefold() == "strict"


class BuildPackage(build_py):
    """Publish staged processor data for strict editable installs."""

    def get_outputs(self, include_bytecode=True):
        if not is_strict_editable(self):
            return super().get_outputs(include_bytecode)
        # Processor mappings are removed below, but their staged destinations
        # must remain outputs so setuptools copies them into the link tree.
        return [output for output in super().get_output_mapping() if not is_generated_package_path(output)]

    def get_output_mapping(self):
        mapping = super().get_output_mapping()
        if not is_strict_editable(self):
            return mapping

        processors_root = Path(self.build_lib).absolute() / "pypcode" / "processors"
        return {
            output: source
            for output, source in mapping.items()
            if not Path(output).absolute().is_relative_to(processors_root)
            and not is_generated_package_path(output)
            and not is_generated_package_path(source)
        }


class BuildExtension(build_ext):
    """
    Runs cmake to build the pypcode_native extension, sleigh binary, and runs sleigh to build .sla files.
    """

    def initialize_options(self):
        super().initialize_options()
        self._strict_editable = False
        self._strict_editable_outputs = []

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
        source_pkg_root_dir = root_dir / "pypcode"
        build_pkg_root_dir = Path(self.build_lib).absolute() / "pypcode"
        self._strict_editable = is_strict_editable(self)
        install_pkg_root_dir = build_pkg_root_dir if self._strict_editable or not self.inplace else source_pkg_root_dir
        target_build_dir = Path(self.build_temp).absolute() / "native"
        host_build_dir = target_build_dir / "host"
        install_pkg_bin_dir = install_pkg_root_dir / "bin"
        host_bin_root_dir = host_build_dir if cross_compiling else install_pkg_bin_dir
        sleigh_filename = "sleigh" + (".exe" if platform.system() == "Windows" else "")
        sleigh_bin = host_bin_root_dir / sleigh_filename
        specfiles_dir = install_pkg_root_dir / "processors"

        if install_pkg_root_dir != source_pkg_root_dir:
            stage_processor_sources(source_pkg_root_dir / "processors", specfiles_dir)

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
            install_pkg_bin_dir.mkdir(parents=True, exist_ok=True)
            ext_path = next(target_build_dir.glob("pypcode_native.*"))
            shutil.copy(target_build_dir / sleigh_filename, install_pkg_bin_dir / sleigh_filename)
            shutil.copy(ext_path, install_pkg_root_dir / ext_path.name)
        else:
            subprocess.check_call(["cmake", "--install", target_build_dir], cwd=root_dir)

        # Build sla files
        subprocess.check_call([sleigh_bin, "-a", specfiles_dir])

        if self._strict_editable:
            extension_output = Path(self.build_lib).absolute() / self.get_ext_filename("pypcode.pypcode_native")
            self._strict_editable_outputs = [
                str(extension_output),
                str(install_pkg_bin_dir / sleigh_filename),
                *(str(path) for path in sorted(specfiles_dir.rglob("*.sla"))),
            ]
            missing_outputs = [path for path in self._strict_editable_outputs if not Path(path).is_file()]
            if missing_outputs:
                raise RuntimeError(f"Strict editable build did not produce expected outputs: {missing_outputs}")

    def get_outputs(self):
        if self._strict_editable:
            return self._strict_editable_outputs.copy()
        return super().get_outputs()

    def get_output_mapping(self):
        if self._strict_editable:
            # The strict editable link tree must copy these files out of the
            # temporary build directory instead of linking to the source tree.
            return {}
        return super().get_output_mapping()


def add_pkg_data_dirs(pkg, dirs):
    pkg_data = []
    for d in dirs:
        for root, directory_names, files in os.walk(os.path.join(pkg, d)):
            directory_names[:] = [name for name in directory_names if not is_generated_package_path(Path(root) / name)]
            r = os.path.relpath(root, pkg)
            pkg_data.extend(
                os.path.join(r, filename) for filename in files if not is_generated_package_path(Path(root) / filename)
            )
    return pkg_data


setup(
    package_data={"pypcode": add_pkg_data_dirs("pypcode", ["docs", "processors"]) + ["py.typed", "pypcode_native.pyi"]},
    cmdclass={"build_ext": BuildExtension, "build_py": BuildPackage},
)
