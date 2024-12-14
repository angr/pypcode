# pylint: disable=missing-class-docstring
from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree import ElementTree as ET


@dataclass
class ExternalName:
    tool: str
    name: str

    @classmethod
    def from_element(cls, element: ET.Element) -> ExternalName:
        return cls(tool=element.attrib["tool"], name=element.attrib["name"])


@dataclass
class Compiler:
    name: str
    spec: str
    id: str

    @classmethod
    def from_element(cls, element: ET.Element) -> Compiler:
        return cls(name=element.attrib["name"], spec=element.attrib["spec"], id=element.attrib["id"])


@dataclass
class Language:
    processor: str
    endian: str
    size: int
    variant: str
    version: str
    slafile: str
    processorspec: str
    id: str
    description: str | None = None
    manualindexfile: str | None = None
    instructionEndian: str | None = None
    compilers: list[Compiler] = field(default_factory=list)
    external_names: list[ExternalName] = field(default_factory=list)

    @classmethod
    def from_element(cls, element: ET.Element) -> Language:
        desc_elem = element.find("description")
        description = desc_elem.text if desc_elem is not None else ""

        return cls(
            processor=element.attrib["processor"],
            endian=element.attrib["endian"],
            size=int(element.attrib["size"]),
            variant=element.attrib["variant"],
            version=element.attrib["version"],
            slafile=element.attrib["slafile"],
            processorspec=element.attrib["processorspec"],
            id=element.attrib["id"],
            description=description,
            manualindexfile=element.attrib.get("manualindexfile"),
            instructionEndian=element.attrib.get("instructionEndian"),
            compilers=[Compiler.from_element(e) for e in element.findall("compiler")],
            external_names=[ExternalName.from_element(e) for e in element.findall("external_name")],
        )


@dataclass
class LanguageDefinitions:
    languages: list[Language] = field(default_factory=list)

    @classmethod
    def from_xml(cls, xml_string: str) -> LanguageDefinitions:
        root = ET.fromstring(xml_string)
        return cls.from_element(root)

    @classmethod
    def from_element(cls, element: ET.Element) -> LanguageDefinitions:
        return cls(languages=[Language.from_element(e) for e in element.findall("language")])
