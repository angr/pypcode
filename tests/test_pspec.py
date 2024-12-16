import unittest
from pathlib import Path

from pypcode.pspec import ProcessorSpec

# Get all .pspec files from processors directory
PROCESSORS_DIR = Path(__file__).parent.parent / "pypcode" / "processors"


class TestProcessorSpec(unittest.TestCase):
    """Test cases for processor spec parsing"""

    def setUp(self):
        self.all_pspecs = list(PROCESSORS_DIR.glob("**/data/languages/*.pspec"))
        self.assertTrue(len(self.all_pspecs) > 0, "No pspec files found")

    def test_all_pspecs(self):
        """Test that we can parse all processor specs without errors."""
        for pspec_path in self.all_pspecs:
            with self.subTest(pspec_path=pspec_path):
                with open(pspec_path, encoding="utf8") as f:
                    pspec = ProcessorSpec.from_xml(f.read())

                # Basic validation of parsed data
                if pspec.programcounter:
                    self.assertIsInstance(pspec.programcounter, str)

                if pspec.context_data:
                    if pspec.context_data.context_set:
                        self.assertIsInstance(pspec.context_data.context_set.space, str)
                        self.assertIsInstance(pspec.context_data.context_set.values, dict)
                        for k, v in pspec.context_data.context_set.values.items():
                            self.assertIsInstance(k, str)
                            self.assertIsInstance(v, int)

                    if pspec.context_data.tracked_set:
                        self.assertIsInstance(pspec.context_data.tracked_set.space, str)
                        self.assertIsInstance(pspec.context_data.tracked_set.values, dict)
                        for k, v in pspec.context_data.tracked_set.values.items():
                            self.assertIsInstance(k, str)
                            self.assertIsInstance(v, int)

                if pspec.register_data:
                    self.assertIsInstance(pspec.register_data.registers, list)
                    for reg in pspec.register_data.registers:
                        self.assertIsInstance(reg.name, str)
                        if reg.group:
                            self.assertIsInstance(reg.group, str)
                        if reg.vector_lane_sizes:
                            self.assertIsInstance(reg.vector_lane_sizes, set)
                            for x in reg.vector_lane_sizes:
                                self.assertIsInstance(x, int)
                        self.assertIsInstance(reg.hidden, bool)

                if pspec.default_symbols:
                    self.assertIsInstance(pspec.default_symbols.symbols, list)
                    for sym in pspec.default_symbols.symbols:
                        self.assertIsInstance(sym.name, str)
                        self.assertIsInstance(sym.address, str)
                        self.assertIsInstance(sym.entry, bool)
                        if sym.type:
                            self.assertIsInstance(sym.type, str)

    def test_x86_pspec(self):
        """Test specific x86 processor spec."""
        pspec_path = PROCESSORS_DIR / "x86" / "data" / "languages" / "x86.pspec"
        with open(pspec_path, encoding="utf8") as f:
            pspec = ProcessorSpec.from_xml(f.read())

        # Test specific x86 properties
        self.assertEqual(pspec.programcounter, "EIP")
        self.assertIn("useOperandReferenceAnalyzerSwitchTables", pspec.properties.properties)
        self.assertEqual(pspec.properties.properties["assemblyRating:x86:LE:32:default"], "GOLD")

        # Test context data
        self.assertIsNotNone(pspec.context_data)
        self.assertIsNotNone(pspec.context_data.context_set)
        self.assertEqual(pspec.context_data.context_set.values["addrsize"], 1)
        self.assertEqual(pspec.context_data.context_set.values["opsize"], 1)

        # Test tracked set
        self.assertIsNotNone(pspec.context_data.tracked_set)
        self.assertEqual(pspec.context_data.tracked_set.values["DF"], 0)

        # Test register data
        self.assertIsNotNone(pspec.register_data)
        reg_names = {r.name for r in pspec.register_data.registers}

        # Test for registers we know are explicitly defined
        self.assertIn("XMM0", reg_names)  # AVX register
        self.assertIn("CF", reg_names)  # Flags register
        self.assertIn("DR0", reg_names)  # Debug register

        # Test AVX registers have correct vector lane sizes
        xmm0 = next(r for r in pspec.register_data.registers if r.name == "XMM0")
        self.assertEqual(xmm0.vector_lane_sizes, {1, 2, 4, 8})

    def test_arm_cortex_pspec(self):
        """Test specific ARM Cortex processor spec."""
        pspec_path = PROCESSORS_DIR / "ARM" / "data" / "languages" / "ARMCortex.pspec"
        with open(pspec_path, encoding="utf8") as f:
            pspec = ProcessorSpec.from_xml(f.read())

        # Test ARM Cortex specific properties
        self.assertEqual(pspec.programcounter, "pc")
        self.assertEqual(pspec.properties.properties["addressesDoNotAppearDirectlyInCode"], "true")

        # Test context data
        self.assertIsNotNone(pspec.context_data)
        self.assertIsNotNone(pspec.context_data.context_set)
        self.assertEqual(pspec.context_data.context_set.values["TMode"], 1)
        self.assertIn("THUMB", pspec.context_data.context_set.description["TMode"])

        # Test default symbols
        self.assertIsNotNone(pspec.default_symbols)
        sym_dict = {s.name: s for s in pspec.default_symbols.symbols}
        self.assertIn("Reset", sym_dict)
        self.assertEqual(sym_dict["Reset"].address, "ram:0x4")
        self.assertTrue(sym_dict["Reset"].entry)
        self.assertEqual(sym_dict["Reset"].type, "code_ptr")

    def test_unknown_elements(self):
        """Test that unknown XML elements don't cause errors."""
        test_xml = """<?xml version="1.0" encoding="UTF-8"?>
        <processor_spec>
            <properties>
                <property key="test" value="value"/>
            </properties>
            <unknown_element>
                <child>test</child>
            </unknown_element>
            <programcounter register="pc"/>
        </processor_spec>
        """
        pspec = ProcessorSpec.from_xml(test_xml)
        self.assertEqual(pspec.properties.properties["test"], "value")
        self.assertEqual(pspec.programcounter, "pc")


if __name__ == "__main__":
    unittest.main()
