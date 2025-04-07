# pylint: disable=missing-class-docstring
from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree import ElementTree as ET


@dataclass
class DataOrganization:
    absolute_max_alignment: int | None = None
    machine_alignment: int | None = None
    default_alignment: int | None = None
    default_pointer_alignment: int | None = None
    wchar_size: int | None = None
    short_size: int | None = None
    integer_size: int | None = None
    long_size: int | None = None
    long_long_size: int | None = None
    float_size: int | None = None
    double_size: int | None = None
    long_double_size: int | None = None
    size_alignment_map: dict[int, int] = field(default_factory=dict)
    bitfield_packing_uses_ms: bool = False

    @classmethod
    def from_element(cls, element: ET.Element) -> DataOrganization:
        if element is None:
            return cls()

        def get_int_attr(elem: ET.Element, attr: str) -> int | None:
            # Handle both attribute and element value cases
            if attr in elem.attrib:
                return int(elem.attrib[attr])
            # Look for a child element with this name
            child = elem.find(attr)
            if child is not None and "value" in child.attrib:
                return int(child.attrib["value"])
            return None

        alignment_map = {}
        map_elem = element.find("size_alignment_map")
        if map_elem is not None:
            for entry in map_elem.findall("entry"):
                size = int(entry.attrib["size"])
                alignment = int(entry.attrib["alignment"])
                alignment_map[size] = alignment

        packing_elem = element.find("bitfield_packing")
        uses_ms = False
        if packing_elem is not None:
            ms_conv = packing_elem.find("use_MS_convention")
            uses_ms = ms_conv is not None and ms_conv.attrib.get("value", "false").lower() == "true"

        return cls(
            absolute_max_alignment=get_int_attr(element, "absolute_max_alignment"),
            machine_alignment=get_int_attr(element, "machine_alignment"),
            default_alignment=get_int_attr(element, "default_alignment"),
            default_pointer_alignment=get_int_attr(element, "default_pointer_alignment"),
            wchar_size=get_int_attr(element, "wchar_size"),
            short_size=get_int_attr(element, "short_size"),
            integer_size=get_int_attr(element, "integer_size"),
            long_size=get_int_attr(element, "long_size"),
            long_long_size=get_int_attr(element, "long_long_size"),
            float_size=get_int_attr(element, "float_size"),
            double_size=get_int_attr(element, "double_size"),
            long_double_size=get_int_attr(element, "long_double_size"),
            size_alignment_map=alignment_map,
            bitfield_packing_uses_ms=uses_ms,
        )


@dataclass
class GlobalScope:
    ram_present: bool = False
    registers: list[str] = field(default_factory=list)

    @classmethod
    def from_element(cls, element: ET.Element) -> GlobalScope:
        if element is None:
            return cls()

        ram_present = any(r.attrib.get("space", "") == "ram" for r in element.findall("range"))
        registers = [r.attrib["name"] for r in element.findall("register")]

        return cls(ram_present=ram_present, registers=registers)


@dataclass
class CompilerSpec:
    data_organization: DataOrganization = field(default_factory=DataOrganization)
    global_scope: GlobalScope = field(default_factory=GlobalScope)
    stackpointer_register: str | None = None
    returnaddress_register: str | None = None
    returnaddress_space: str | None = None
    returnaddress_offset: int | None = None
    returnaddress_size: int | None = None

    @classmethod
    def from_xml(cls, xml_string: str) -> CompilerSpec:
        root = ET.fromstring(xml_string)
        return cls.from_element(root)

    @classmethod
    def from_element(cls, element: ET.Element) -> CompilerSpec:
        data_org_elem = element.find("data_organization")
        data_org = DataOrganization.from_element(data_org_elem) if data_org_elem is not None else DataOrganization()
        global_elem = element.find("global")
        global_scope = GlobalScope.from_element(global_elem) if global_elem is not None else GlobalScope()

        sp_elem = element.find("stackpointer")
        stackpointer = sp_elem.attrib["register"] if sp_elem is not None else None

        ret_elem = element.find("returnaddress")
        retaddr_reg = retaddr_space = None
        retaddr_offset = retaddr_size = None
        if ret_elem is not None:
            if "register" in ret_elem.attrib:
                retaddr_reg = ret_elem.attrib["register"]
            else:
                var_elem = ret_elem.find("varnode")
                if var_elem is not None:
                    retaddr_space = var_elem.attrib["space"]
                    retaddr_offset = int(var_elem.attrib["offset"])
                    retaddr_size = int(var_elem.attrib["size"])

        return cls(
            data_organization=data_org,
            global_scope=global_scope,
            stackpointer_register=stackpointer,
            returnaddress_register=retaddr_reg,
            returnaddress_space=retaddr_space,
            returnaddress_offset=retaddr_offset,
            returnaddress_size=retaddr_size,
        )
