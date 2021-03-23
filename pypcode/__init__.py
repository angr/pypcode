#!/usr/bin/env python
import cppyy
import sys
import logging
import os.path
import xml.etree.ElementTree as ET
from typing import Generator, Sequence

log = logging.getLogger(__name__)

PYPCODENATIVE_PATH=os.path.join(os.path.dirname(__file__), 'pypcode-native')
SLEIGH_SRC_PATH=os.path.join(PYPCODENATIVE_PATH, 'sleigh')
SLEIGH_SPECFILES_PATH=os.path.join(PYPCODENATIVE_PATH, 'processors')

log.debug('Loading Library')
cppyy.include(os.path.join(PYPCODENATIVE_PATH, 'pypcode-native.h'))
cppyy.include(os.path.join(SLEIGH_SRC_PATH, 'translate.hh'))
cppyy.include(os.path.join(SLEIGH_SRC_PATH, 'error.hh'))
cppyy.load_library(os.path.join(PYPCODENATIVE_PATH, 'pypcode-native.so'))

# Import names into this namespace
from cppyy.gbl import Address
from cppyy.gbl import AssemblyEmitCacher
from cppyy.gbl import AddrSpace
from cppyy.gbl import ContextInternal
from cppyy.gbl import DocumentStorage
from cppyy.gbl import Element
from cppyy.gbl import get_opname
from cppyy.gbl import PcodeRawOutHelper
from cppyy.gbl import SimpleLoadImage
from cppyy.gbl import Sleigh
from cppyy.gbl import OpCode
from cppyy.gbl import VarnodeData
from cppyy.gbl import PcodeOpRaw

class ArchLanguage:
  """
  Encapsulates a particular language for an architecture as defined in a *.ldefs
  file for an arch.
  """

  __slots__ = (
    "archdir",
    "ldef"
    )

  archdir: str
  ldef: ET.Element

  def __init__(self, archdir: str, ldef: ET.Element):
    self.archdir = archdir
    self.ldef = ldef

  @property
  def pspec_path(self) -> str:
    return os.path.join(self.archdir, self.processorspec)

  @property
  def slafile_path(self) -> str:
    return os.path.join(self.archdir, self.slafile)

  @property
  def description(self) -> str:
    return self.ldef.find('description').text

  def __getattr__(self, key):
    if key in self.ldef.attrib:
      return self.ldef.attrib[key]
    super().__attr__(key)

  def init_context_from_pspec(self, context:ContextInternal) -> None:
    pspec = ET.parse(self.pspec_path)
    cd = pspec.getroot().find('context_data')
    if cd is None: return
    cs = cd.find('context_set')
    if cs is None: return
    for e in cs:
      assert(e.tag == 'set')
      context.setVariableDefault(e.attrib['name'], int(e.attrib['val']))

class Arch:
  """
  Encapsulates information about a particular architecture. An architecture
  can have many 'languages'. Query the `languages` property for a list of all
  supported languages.
  """

  __slots__ = (
    "archpath",
    "archname",
    "ldefpath",
    "ldef",
    "languages",
    )

  archpath: str
  archname: str
  ldefpath: str
  ldef: ET.ElementTree
  languages: Sequence[ArchLanguage]

  def __init__(self, archname: str, ldefpath: str):
    self.archpath = os.path.dirname(ldefpath)
    self.archname = archname
    self.ldefpath = ldefpath
    self.ldef = ET.parse(ldefpath)
    self.languages = [ArchLanguage(self.archpath, e) for e in self.ldef.getroot()]

  @classmethod
  def enumerate(cls) -> Generator['Arch', None, None]:
    # processors/<architecture>/data/languages/<variant>.ldefs
    for archname in os.listdir(SLEIGH_SPECFILES_PATH):
      langdir = os.path.join(SLEIGH_SPECFILES_PATH, archname, 'data', 'languages')
      if not (os.path.exists(langdir) and os.path.isdir(langdir)): continue
      for langname in os.listdir(langdir):
        if not langname.endswith('.ldefs'): continue
        ldefpath = os.path.join(langdir, langname)
        yield Arch(archname, ldefpath)

