import unittest
from pathlib import Path

from pypcode.cspec import CompilerSpec

# Get all .cspec files from processors directory
PROCESSORS_DIR = Path(__file__).parent.parent / "pypcode" / "processors"


class TestCompilerSpec(unittest.TestCase):
    """Test cases for compiler spec parsing"""

    def setUp(self):
        self.all_cspecs = list(PROCESSORS_DIR.glob("**/data/languages/*.cspec"))
        self.assertTrue(len(self.all_cspecs) > 0, "No cspec files found")

    def test_all_cspecs(self):
        """Test that we can parse all compiler specs without errors."""
        for cspec_path in self.all_cspecs:
            with self.subTest(cspec_path=cspec_path):
                with open(cspec_path, encoding="utf8") as f:
                    cspec = CompilerSpec.from_xml(f.read())

                # Basic validation of parsed data
                self.assertIsNotNone(cspec.data_organization)
                self.assertIsNotNone(cspec.global_scope)

    def test_x86_64_win_cspec(self):
        """Test specific x86-64 Windows compiler spec."""
        cspec_path = PROCESSORS_DIR / "x86" / "data" / "languages" / "x86-64-win.cspec"
        with open(cspec_path, encoding="utf8") as f:
            cspec = CompilerSpec.from_xml(f.read())

        # Test data organization
        data_org = cspec.data_organization
        self.assertEqual(data_org.wchar_size, 2)
        self.assertEqual(data_org.long_size, 4)
        self.assertEqual(data_org.long_long_size, 8)

        # Test size alignment map
        self.assertEqual(data_org.size_alignment_map[1], 1)
        self.assertEqual(data_org.size_alignment_map[2], 2)
        self.assertEqual(data_org.size_alignment_map[4], 4)
        self.assertEqual(data_org.size_alignment_map[8], 8)

        # Test bitfield packing
        self.assertTrue(data_org.bitfield_packing_uses_ms)

        # Test global scope
        self.assertTrue(cspec.global_scope.ram_present)
        self.assertIn("MXCSR", cspec.global_scope.registers)

        # Test stack and return info
        self.assertEqual(cspec.stackpointer_register, "RSP")
        self.assertEqual(cspec.returnaddress_space, "stack")
        self.assertEqual(cspec.returnaddress_offset, 0)
        self.assertEqual(cspec.returnaddress_size, 8)

    def test_x86_64_gcc_cspec(self):
        """Test specific x86-64 GCC compiler spec."""
        cspec_path = PROCESSORS_DIR / "x86" / "data" / "languages" / "x86-64-gcc.cspec"
        with open(cspec_path, encoding="utf8") as f:
            cspec = CompilerSpec.from_xml(f.read())

        # Test data organization
        data_org = cspec.data_organization
        self.assertEqual(data_org.wchar_size, 4)
        self.assertEqual(data_org.long_size, 8)
        self.assertEqual(data_org.long_double_size, 10)  # Note: aligned length is 16

        # Test size alignment map
        self.assertEqual(data_org.size_alignment_map[1], 1)
        self.assertEqual(data_org.size_alignment_map[2], 2)
        self.assertEqual(data_org.size_alignment_map[4], 4)
        self.assertEqual(data_org.size_alignment_map[8], 8)
        self.assertEqual(data_org.size_alignment_map[16], 16)

        # Test global scope
        self.assertTrue(cspec.global_scope.ram_present)
        self.assertIn("MXCSR", cspec.global_scope.registers)

        # Test stack and return info
        self.assertEqual(cspec.stackpointer_register, "RSP")
        self.assertEqual(cspec.returnaddress_space, "stack")
        self.assertEqual(cspec.returnaddress_offset, 0)
        self.assertEqual(cspec.returnaddress_size, 8)

    def test_aarch64_cspec(self):
        """Test specific AArch64 compiler spec."""
        cspec_path = PROCESSORS_DIR / "AARCH64" / "data" / "languages" / "AARCH64.cspec"
        with open(cspec_path, encoding="utf8") as f:
            cspec = CompilerSpec.from_xml(f.read())

        # Test data organization
        data_org = cspec.data_organization
        self.assertEqual(data_org.wchar_size, 4)
        self.assertEqual(data_org.long_size, 8)
        self.assertEqual(data_org.double_size, 8)

        # Test size alignment map
        self.assertEqual(data_org.size_alignment_map[1], 1)
        self.assertEqual(data_org.size_alignment_map[2], 2)
        self.assertEqual(data_org.size_alignment_map[4], 4)
        self.assertEqual(data_org.size_alignment_map[8], 8)
        self.assertEqual(data_org.size_alignment_map[16], 16)

        # Test global scope
        self.assertTrue(cspec.global_scope.ram_present)

        # Test stack pointer
        self.assertEqual(cspec.stackpointer_register, "sp")

    def test_x86_32_gcc_cspec(self):
        """Test specific x86 32-bit GCC compiler spec."""
        cspec_path = PROCESSORS_DIR / "x86" / "data" / "languages" / "x86gcc.cspec"
        with open(cspec_path, encoding="utf8") as f:
            cspec = CompilerSpec.from_xml(f.read())

        # Test data organization
        data_org = cspec.data_organization
        self.assertEqual(data_org.wchar_size, 4)
        self.assertEqual(data_org.long_size, 4)
        self.assertEqual(data_org.long_long_size, 8)

        # Test size alignment map
        self.assertEqual(data_org.size_alignment_map[1], 1)
        self.assertEqual(data_org.size_alignment_map[2], 2)
        self.assertEqual(data_org.size_alignment_map[4], 4)
        self.assertEqual(data_org.size_alignment_map[8], 4)

        # Test global scope
        self.assertTrue(cspec.global_scope.ram_present)
        self.assertIn("MXCSR", cspec.global_scope.registers)

        # Test stack and return info
        self.assertEqual(cspec.stackpointer_register, "ESP")
        self.assertEqual(cspec.returnaddress_space, "stack")
        self.assertEqual(cspec.returnaddress_offset, 0)
        self.assertEqual(cspec.returnaddress_size, 4)  # 32-bit return address

    def test_arm_32_cspec(self):
        """Test specific ARM 32-bit compiler spec."""
        cspec_path = PROCESSORS_DIR / "ARM" / "data" / "languages" / "ARM.cspec"
        with open(cspec_path, encoding="utf8") as f:
            cspec = CompilerSpec.from_xml(f.read())

        # Test data organization
        data_org = cspec.data_organization
        self.assertEqual(data_org.wchar_size, 4)
        self.assertEqual(data_org.long_size, 4)
        self.assertEqual(data_org.double_size, 8)

        # Test size alignment map
        self.assertEqual(data_org.size_alignment_map[1], 1)
        self.assertEqual(data_org.size_alignment_map[2], 2)
        self.assertEqual(data_org.size_alignment_map[4], 4)
        self.assertEqual(data_org.size_alignment_map[8], 8)

        # Test global scope
        self.assertTrue(cspec.global_scope.ram_present)

        # Test stack pointer
        self.assertEqual(cspec.stackpointer_register, "sp")


if __name__ == "__main__":
    unittest.main()
