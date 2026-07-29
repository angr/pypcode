import hashlib
import json
import os
import runpy
import stat
import subprocess
import sys
import sysconfig
import tempfile
import unittest
from pathlib import Path
from unittest import mock


def _snapshot_tree(root: Path):
    snapshot = {}
    for path in (root, *sorted(root.rglob("*"))):
        relative = path.relative_to(root).as_posix() or "."
        metadata = path.lstat()
        kind = stat.S_IFMT(metadata.st_mode)
        if path.is_symlink():
            payload = os.readlink(path)
        elif path.is_file():
            payload = hashlib.sha256(path.read_bytes()).hexdigest()
        else:
            payload = ""
        size = metadata.st_size if path.is_file() or path.is_symlink() else 0
        modified = metadata.st_mtime_ns if path.is_file() or path.is_symlink() else 0
        snapshot[relative] = (
            kind,
            stat.S_IMODE(metadata.st_mode),
            size,
            modified,
            payload,
        )
    return snapshot


def _relative_files(root: Path):
    return {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}


def _load_setup_module(repository: Path):
    with mock.patch("setuptools.setup"):
        return runpy.run_path(str(repository / "setup.py"))


class EditableModeTest(unittest.TestCase):
    """Match setuptools' case-insensitive editable-mode semantics."""

    def test_only_strict_mode_uses_staged_outputs(self):
        repository = Path(__file__).resolve().parents[1]
        is_strict_editable = _load_setup_module(repository)["is_strict_editable"]

        for mode, expected in (("strict", True), ("STRICT", True), ("Strict", True), ("lenient", False), (None, False)):
            with self.subTest(mode=mode):
                distribution = mock.Mock()
                distribution.get_command_obj.return_value = mock.Mock(mode=mode)
                command = mock.Mock(editable_mode=True, distribution=distribution)
                self.assertEqual(is_strict_editable(command), expected)

        distribution = mock.Mock()
        command = mock.Mock(editable_mode=False, distribution=distribution)
        self.assertFalse(is_strict_editable(command))
        distribution.get_command_obj.assert_not_called()


class ProcessorStagingTest(unittest.TestCase):
    """Check that a reused build directory is an exact source projection."""

    def test_staging_replaces_persistent_tree_and_excludes_generated_files(self):
        repository = Path(__file__).resolve().parents[1]
        setup_module = _load_setup_module(repository)
        stage_processor_sources = setup_module["stage_processor_sources"]

        with tempfile.TemporaryDirectory(prefix="pypcode-processor-staging-") as temporary_directory:
            temporary_root = Path(temporary_directory)
            source = temporary_root / "source"
            destination = temporary_root / "persistent-build" / "pypcode" / "processors"
            (source / "arch" / "data").mkdir(parents=True)
            (source / "arch" / "data" / "old.ldefs").write_text("old\n", encoding="utf-8")
            (source / "arch" / "data" / "manual.idx").write_text("index\n", encoding="utf-8")
            (source / "arch" / "data" / "generated.sla").write_bytes(b"sla")
            (source / "arch" / "data" / "native.so").write_bytes(b"so")
            (source / "arch" / "data" / "native.pyd").write_bytes(b"pyd")
            (source / "arch" / "data" / "legacy.pyo").write_bytes(b"pyo")
            (source / "arch" / "data" / "__pycache__").mkdir()
            (source / "arch" / "data" / "__pycache__" / "cached.pyc").write_bytes(b"pyc")

            (destination / "removed" / "data").mkdir(parents=True)
            (destination / "removed" / "data" / "stale.ldefs").write_text("stale\n", encoding="utf-8")
            stage_processor_sources(source, destination)

            self.assertEqual(
                _relative_files(destination),
                {"arch/data/manual.idx", "arch/data/old.ldefs"},
            )

            (source / "arch" / "data" / "old.ldefs").unlink()
            (source / "arch" / "data" / "new.ldefs").write_text("new\n", encoding="utf-8")
            (destination / "arch" / "data" / "orphaned.ldefs").write_text("orphan\n", encoding="utf-8")
            (destination / "arch" / "data" / "orphaned.sla").write_bytes(b"sla")
            stage_processor_sources(source, destination)

            self.assertEqual(
                _relative_files(destination),
                {"arch/data/manual.idx", "arch/data/new.ldefs"},
            )


@unittest.skipUnless(
    os.environ.get("PYPCODE_RUN_STRICT_EDITABLE_TEST") == "1",
    "set PYPCODE_RUN_STRICT_EDITABLE_TEST=1 in a disposable Python environment",
)
class StrictEditableInstallTest(unittest.TestCase):
    """Exercise the complete strict-editable packaging and runtime path."""

    def test_install_ignores_removable_artifacts_and_translates_x86_real_mode(self):
        repository = Path(__file__).resolve().parents[1]
        source_package = repository / "pypcode"
        before_seeding = _snapshot_tree(source_package)
        environment = os.environ.copy()
        environment.pop("PYTHONHOME", None)
        environment.pop("PYTHONPATH", None)
        environment.update(
            {
                "CMAKE_BUILD_PARALLEL_LEVEL": "1",
                "PATH": os.pathsep.join((str(Path(sys.executable).parent), environment.get("PATH", ""))),
                "PIP_DISABLE_PIP_VERSION_CHECK": "1",
                "PYTHONDONTWRITEBYTECODE": "1",
            }
        )

        extension_suffix = sysconfig.get_config_var("EXT_SUFFIX")
        self.assertIsInstance(extension_suffix, str)
        seeded_files = [
            source_package / f"pypcode_native{extension_suffix}",
            source_package / "__pycache__" / "strict_editable_seed.pyc",
            source_package / "docs" / "strict_editable_seed.pyo",
            source_package / "processors" / "__pycache__" / "strict_editable_seed.pyc",
            source_package / "processors" / "strict_editable_seed.sla",
            source_package / "processors" / "strict_editable_seed.so",
            source_package / "processors" / "strict_editable_seed.pyd",
            source_package / "bin" / ("sleigh.exe" if os.name == "nt" else "sleigh"),
        ]
        for seeded_file in seeded_files:
            self.assertFalse(
                seeded_file.exists() or seeded_file.is_symlink(),
                msg=f"strict-editable integration test requires a clean disposable source tree: {seeded_file}",
            )

        probe = """
import json
import os
from pathlib import Path

import pypcode
import pypcode.pypcode_native

language = pypcode.ArchLanguage.from_id("x86:LE:16:Real Mode")
assert language is not None
translation = pypcode.Context(language).translate(
    b"\\x90\\xc3",
    base_address=0x1000,
    max_instructions=2,
)
assert translation.ops
assert translation.ops[0].opcode == pypcode.OpCode.IMARK
print(json.dumps({
    "package": str(Path(pypcode.__file__).parent),
    "extension": pypcode.pypcode_native.__file__,
    "ldef": str(Path(language.archdir) / "x86.ldefs"),
    "pspec": language.pspec_path,
    "sla": language.slafile_path,
    "sleigh": str(Path(pypcode.__file__).parent / "bin" / ("sleigh.exe" if os.name == "nt" else "sleigh")),
}))
"""
        created_directories = set()
        try:
            for seeded_file in seeded_files:
                parent = seeded_file.parent
                while not parent.exists():
                    created_directories.add(parent)
                    parent = parent.parent
                seeded_file.parent.mkdir(parents=True, exist_ok=True)
                seeded_file.write_bytes(b"source artifact that strict editable must ignore\n")
            after_seeding = _snapshot_tree(source_package)

            with tempfile.TemporaryDirectory(prefix="pypcode-egg-info-") as egg_base:
                egg_info = subprocess.run(
                    [sys.executable, "setup.py", "egg_info", "--egg-base", egg_base],
                    check=False,
                    capture_output=True,
                    cwd=repository,
                    env=environment,
                    text=True,
                )
                self.assertEqual(
                    egg_info.returncode,
                    0,
                    msg=f"stdout:\n{egg_info.stdout}\n\nstderr:\n{egg_info.stderr}",
                )
                sources_file = next(Path(egg_base).glob("*.egg-info/SOURCES.txt"))
                manifest_paths = sources_file.read_text(encoding="utf-8").splitlines()
                generated_manifest_paths = [
                    path
                    for path in manifest_paths
                    if "__pycache__" in Path(path).parts
                    or Path(path).suffix.casefold() in {".pyc", ".pyd", ".pyo", ".sla", ".so"}
                    or Path(path).parts[:2] == ("pypcode", "bin")
                ]
                self.assertEqual(generated_manifest_paths, [])

            install = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "--no-build-isolation",
                    "--no-deps",
                    "--config-settings",
                    "editable_mode=STRICT",
                    "--editable",
                    str(repository),
                ],
                check=False,
                capture_output=True,
                env=environment,
                text=True,
            )

            self.assertEqual(after_seeding, _snapshot_tree(source_package))
            self.assertEqual(
                install.returncode,
                0,
                msg=f"stdout:\n{install.stdout}\n\nstderr:\n{install.stderr}",
            )

            resources = self._run_probe(probe, environment)
            package = Path(resources.pop("package"))
            for name, resource in resources.items():
                path = Path(resource)
                self.assertTrue(path.exists(), msg=f"{name} is missing: {path}")
                self.assertFalse(
                    path.resolve().is_relative_to(source_package.resolve()),
                    msg=f"{name} resolves into the source package: {path}",
                )
            self.assertFalse(package.resolve().is_relative_to(source_package.resolve()))
            copied_seed_artifacts = [path for path in package.rglob("*") if "strict_editable_seed" in path.name]
            self.assertEqual(copied_seed_artifacts, [])
            self.assertEqual(after_seeding, _snapshot_tree(source_package))

            for seeded_file in reversed(seeded_files):
                seeded_file.unlink()
            for directory in sorted(created_directories, key=lambda path: len(path.parts), reverse=True):
                if directory.exists() and not any(directory.iterdir()):
                    directory.rmdir()
            self.assertEqual(before_seeding, _snapshot_tree(source_package))

            broken_links = [path for path in package.rglob("*") if path.is_symlink() and not path.exists()]
            self.assertEqual(broken_links, [])
            self._run_probe(probe, environment)
            self.assertEqual(before_seeding, _snapshot_tree(source_package))
        finally:
            for seeded_file in reversed(seeded_files):
                if seeded_file.exists() or seeded_file.is_symlink():
                    seeded_file.unlink()
            for directory in sorted(created_directories, key=lambda path: len(path.parts), reverse=True):
                if directory.exists() and not any(directory.iterdir()):
                    directory.rmdir()

    def _run_probe(self, probe, environment):
        with tempfile.TemporaryDirectory(prefix="pypcode-editable-probe-") as probe_directory:
            runtime = subprocess.run(
                [sys.executable, "-c", probe],
                check=False,
                capture_output=True,
                cwd=probe_directory,
                env=environment,
                text=True,
            )
        self.assertEqual(
            runtime.returncode,
            0,
            msg=f"stdout:\n{runtime.stdout}\n\nstderr:\n{runtime.stderr}",
        )
        return json.loads(runtime.stdout)


if __name__ == "__main__":
    unittest.main()
