import unittest
from pathlib import Path

from pypcode.ldefs import LanguageDefinitions

# Get all .ldefs files from processors directory
PROCESSORS_DIR = Path(__file__).parent.parent / "pypcode" / "processors"


class TestLanguageDefinitions(unittest.TestCase):
    """Test cases for language definition parsing"""

    def setUp(self):
        self.all_ldefs = list(PROCESSORS_DIR.glob("**/data/languages/*.ldefs"))
        self.assertTrue(len(self.all_ldefs) > 0, "No ldefs files found")

    def test_all_ldefs(self):
        """Test that we can parse all language definition files without errors."""
        for ldefs_path in self.all_ldefs:
            with self.subTest(ldefs_path=ldefs_path):
                with open(ldefs_path, encoding="utf8") as f:
                    ldefs = LanguageDefinitions.from_xml(f.read())

                # Basic validation of parsed data
                self.assertIsNotNone(ldefs.languages)
                for lang in ldefs.languages:
                    self.assertIsInstance(lang.processor, str)
                    self.assertIsInstance(lang.endian, str)
                    self.assertIsInstance(lang.size, int)
                    self.assertIsInstance(lang.variant, str)
                    self.assertIsInstance(lang.version, str)
                    self.assertIsInstance(lang.slafile, str)
                    self.assertIsInstance(lang.processorspec, str)
                    self.assertIsInstance(lang.id, str)

    def test_x86_ldefs(self):
        """Test specific x86 language definitions."""
        ldefs_path = PROCESSORS_DIR / "x86" / "data" / "languages" / "x86.ldefs"
        with open(ldefs_path, encoding="utf8") as f:
            ldefs = LanguageDefinitions.from_xml(f.read())

        # Test basic properties
        x86_default = next(ldef for ldef in ldefs.languages if ldef.variant == "default")
        self.assertEqual(x86_default.processor, "x86")
        self.assertEqual(x86_default.endian, "little")
        self.assertEqual(x86_default.size, 32)
        self.assertEqual(x86_default.id, "x86:LE:32:default")
        self.assertEqual(x86_default.description, "Intel/AMD 32-bit x86")

        # Test compiler specs
        compiler_names = {c.name for c in x86_default.compilers}
        self.assertIn("Visual Studio", compiler_names)
        self.assertIn("gcc", compiler_names)
        self.assertIn("golang", compiler_names)

        vs_compiler = next(c for c in x86_default.compilers if c.name == "Visual Studio")
        self.assertEqual(vs_compiler.spec, "x86win.cspec")
        self.assertEqual(vs_compiler.id, "windows")

        # Test external names
        external_tools = {e.tool for e in x86_default.external_names}
        self.assertIn("gnu", external_tools)
        self.assertIn("IDA-PRO", external_tools)
        self.assertIn("DWARF.register.mapping.file", external_tools)

        ida_names = [e.name for e in x86_default.external_names if e.tool == "IDA-PRO"]
        self.assertIn("metapc", ida_names)

    def test_arm_ldefs(self):
        """Test specific ARM language definitions."""
        ldefs_path = PROCESSORS_DIR / "ARM" / "data" / "languages" / "ARM.ldefs"
        with open(ldefs_path, encoding="utf8") as f:
            ldefs = LanguageDefinitions.from_xml(f.read())

        # Test that we have both BE and LE variants
        variants = {ldef.endian for ldef in ldefs.languages}
        self.assertIn("big", variants)
        self.assertIn("little", variants)

        # Test ARM v8 little endian variant
        arm_v8_le = next(ldef for ldef in ldefs.languages if ldef.id == "ARM:LE:32:v8")
        self.assertEqual(arm_v8_le.processor, "ARM")
        self.assertEqual(arm_v8_le.size, 32)
        self.assertEqual(arm_v8_le.variant, "v8")
        self.assertEqual(arm_v8_le.slafile, "ARM8_le.sla")
        self.assertEqual(arm_v8_le.description, "Generic ARM/Thumb v8 little endian")

        # Test compilers
        compiler_dict = {c.id: c for c in arm_v8_le.compilers}
        self.assertIn("default", compiler_dict)
        self.assertIn("windows", compiler_dict)
        self.assertEqual(compiler_dict["windows"].name, "Visual Studio")
        self.assertEqual(compiler_dict["windows"].spec, "ARM_win.cspec")

        # Test external names
        external_dict = {e.tool: e.name for e in arm_v8_le.external_names}
        self.assertEqual(external_dict["qemu"], "qemu-arm")
        self.assertEqual(external_dict["IDA-PRO"], "arm")
        self.assertEqual(external_dict["DWARF.register.mapping.file"], "ARMneon.dwarf")


if __name__ == "__main__":
    unittest.main()
