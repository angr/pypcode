#!/usr/bin/env python
import cppyy
import sys
import logging
import os.path

log = logging.getLogger(__name__)

PYPCODENATIVE_PATH=os.path.join(os.path.dirname(__file__), 'pypcode-native')
SLEIGH_SRC_PATH=os.path.join(PYPCODENATIVE_PATH, 'sleigh')
SLEIGH_SPECFILES_PATH=os.path.join(PYPCODENATIVE_PATH, 'processors')

log.debug('Loading Library')
cppyy.include(os.path.join(PYPCODENATIVE_PATH, 'pypcode-native.h'))
cppyy.include(os.path.join(SLEIGH_SRC_PATH, 'translate.hh'))
cppyy.include(os.path.join(SLEIGH_SRC_PATH, 'error.hh'))
cppyy.load_library(os.path.join(PYPCODENATIVE_PATH, 'pypcode-native.so'))

class AssemblyEmitCacher(cppyy.gbl.AssemblyEmit):
  def dump(self, addr, mnem, body):
    self.addr = addr
    self.mnem = mnem
    self.body = body

# Import names into this namespace
from cppyy.gbl import Address
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
