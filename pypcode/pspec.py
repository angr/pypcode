# pylint: disable=missing-class-docstring
from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree import ElementTree as ET


@dataclass
class Property:
    key: str
    value: str

    @classmethod
    def from_element(cls, element: ET.Element) -> Property:
        return cls(key=element.attrib["key"], value=element.attrib["value"])


@dataclass
class Properties:
    properties: dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_element(cls, element: ET.Element) -> Properties:
        props = cls()
        if element is not None:
            for prop in element.findall("property"):
                p = Property.from_element(prop)
                props.properties[p.key] = p.value
        return props


@dataclass
class ContextSet:
    space: str
    values: dict[str, int]
    description: dict[str, str]

    @classmethod
    def from_element(cls, element: ET.Element) -> ContextSet:
        values = {}
        descriptions = {}
        for set_elem in element.findall("set"):
            name = set_elem.attrib["name"]
            values[name] = int(set_elem.attrib["val"])
            if "description" in set_elem.attrib:
                descriptions[name] = set_elem.attrib["description"]
        return cls(space=element.attrib["space"], values=values, description=descriptions)


@dataclass
class TrackedSet:
    space: str
    values: dict[str, int]

    @classmethod
    def from_element(cls, element: ET.Element) -> TrackedSet:
        values = {}
        for set_elem in element.findall("set"):
            val_str = set_elem.attrib["val"]
            if val_str.startswith("0x"):
                values[set_elem.attrib["name"]] = int(val_str, 16)
            else:
                values[set_elem.attrib["name"]] = int(val_str)
        return cls(space=element.attrib["space"], values=values)


@dataclass
class ContextData:
    context_set: ContextSet | None = None
    tracked_set: TrackedSet | None = None

    @classmethod
    def from_element(cls, element: ET.Element) -> ContextData:
        context_set_elem = element.find("context_set")
        tracked_set_elem = element.find("tracked_set")

        return cls(
            context_set=ContextSet.from_element(context_set_elem) if context_set_elem is not None else None,
            tracked_set=TrackedSet.from_element(tracked_set_elem) if tracked_set_elem is not None else None,
        )


@dataclass
class Register:
    name: str
    group: str | None = None
    vector_lane_sizes: set[int] | None = None
    hidden: bool = False

    @classmethod
    def from_element(cls, element: ET.Element) -> Register:
        vector_sizes = None
        if "vector_lane_sizes" in element.attrib:
            vector_sizes = {int(x) for x in element.attrib["vector_lane_sizes"].split(",")}

        return cls(
            name=element.attrib["name"],
            group=element.attrib.get("group"),
            vector_lane_sizes=vector_sizes,
            hidden=element.attrib.get("hidden", "false").lower() == "true",
        )


@dataclass
class RegisterData:
    registers: list[Register] = field(default_factory=list)

    @classmethod
    def from_element(cls, element: ET.Element) -> RegisterData:
        registers = []
        if element is not None:
            for reg in element.findall("register"):
                registers.append(Register.from_element(reg))
        return cls(registers=registers)


@dataclass
class DefaultSymbol:
    name: str
    address: str
    entry: bool
    type: str | None = None

    @classmethod
    def from_element(cls, element: ET.Element) -> DefaultSymbol:
        return cls(
            name=element.attrib["name"],
            address=element.attrib["address"],
            entry=element.attrib.get("entry", "false").lower() == "true",
            type=element.attrib.get("type"),
        )


@dataclass
class DefaultSymbols:
    symbols: list[DefaultSymbol] = field(default_factory=list)

    @classmethod
    def from_element(cls, element: ET.Element) -> DefaultSymbols:
        symbols = []
        if element is not None:
            for sym in element.findall("symbol"):
                symbols.append(DefaultSymbol.from_element(sym))
        return cls(symbols=symbols)


@dataclass
class ProcessorSpec:
    properties: Properties | None
    programcounter: str | None
    context_data: ContextData | None
    register_data: RegisterData | None
    default_symbols: DefaultSymbols | None
    incidentalcopy: list[str] | None = None

    @classmethod
    def from_xml(cls, xml_string: str) -> ProcessorSpec:
        root = ET.fromstring(xml_string)
        return cls.from_element(root)

    @classmethod
    def from_element(cls, element: ET.Element) -> ProcessorSpec:
        props_elem = element.find("properties")
        props = Properties.from_element(props_elem) if props_elem is not None else None

        pc_elem = element.find("programcounter")
        pc_reg = pc_elem.attrib["register"] if pc_elem is not None else None

        context_data_elem = element.find("context_data")
        context_data = ContextData.from_element(context_data_elem) if context_data_elem is not None else None

        register_data_elem = element.find("register_data")
        register_data = RegisterData.from_element(register_data_elem) if register_data_elem is not None else None

        default_symbols_elem = element.find("default_symbols")
        default_symbols = (
            DefaultSymbols.from_element(default_symbols_elem) if default_symbols_elem is not None else None
        )

        incidentalcopy = []
        incidentalcopy_elem = element.find("incidentalcopy")
        if incidentalcopy_elem is not None:
            for reg in incidentalcopy_elem.findall("register"):
                incidentalcopy.append(reg.attrib["name"])

        return cls(
            properties=props,
            programcounter=pc_reg,
            context_data=context_data,
            register_data=register_data,
            default_symbols=default_symbols,
            incidentalcopy=incidentalcopy if incidentalcopy else None,
        )
