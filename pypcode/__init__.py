#!/usr/bin/env python
# Based on sleighexample.cc

import cppyy
import sys
import logging
import os.path

log = logging.getLogger(__name__)

PYPCODENATIVE_PATH=os.path.join(os.path.dirname(__file__), 'pypcode-native')
SLEIGH_PATH=os.path.join(PYPCODENATIVE_PATH, 'sleigh-2.1.0')
SLEIGH_SRC_PATH=os.path.join(SLEIGH_PATH, 'src')
SLEIGH_SPECFILES_PATH=os.path.join(SLEIGH_PATH, 'specfiles')

log.debug('Loading Headers')
cppyy.include(os.path.join(SLEIGH_SRC_PATH, 'loadimage.hh'))
cppyy.include(os.path.join(SLEIGH_SRC_PATH, 'sleigh.hh'))

log.debug('Loading Library')
cppyy.load_library(os.path.join(PYPCODENATIVE_PATH, 'pypcode-native.so'))

# FIXME: Move to pypcode-native
log.debug('Creating Loader')
cppyy.cppdef('''
// This is a tiny LoadImage class which feeds the executable bytes to the translator
class SimpleLoadImage : public LoadImage {
  uintb baseaddr;
  int4 length;
  uint1 *data;
public:
  SimpleLoadImage(uintb ad,uint1 *ptr,int4 sz) : LoadImage("nofile") { baseaddr = ad; data = ptr; length = sz; }
  virtual void loadFill(uint1 *ptr,int4 size,const Address &addr);
  virtual string getArchType(void) const { return "myload"; }
  virtual void adjustVma(long adjust) { }
};

// This is the only important method for the LoadImage. It returns bytes from the static array
// depending on the address range requested
void SimpleLoadImage::loadFill(uint1 *ptr,int4 size,const Address &addr)
{
  uintb start = addr.getOffset();
  uintb max = baseaddr + (length-1);
  for(int4 i=0;i<size;++i) {  // For every byte requestes
    uintb curoff = start + i; // Calculate offset of byte
    if ((curoff < baseaddr)||(curoff>max)) {  // If byte does not fall in window
      ptr[i] = 0;   // return 0
      continue;
    }
    uintb diff = curoff - baseaddr;
    ptr[i] = data[(int4)diff];  // Otherwise return data from our window
  }
}
''')

#
# Define a helper class that recieves pcode ops from the translator and caches
# them in member variables to be accessed from Python side
#
# FIXME: Move to pypcode-native
log.debug('Creating p-code helper class')
cppyy.cppdef('''
class PcodeRawOutHelper : public PcodeEmit {
public:
  vector<PcodeOpRaw *> opcache;  ///< The cache of current p-code ops
  vector<VarnodeData *> varcache;  ///< The cache of current varnodes
  vector<OpBehavior *> inst; ///< Array of behaviors for translating OpCode
  uintm uniq;       ///< Starting offset for defining temporaries in unique space

  VarnodeData *createVarnode(const VarnodeData *var); ///< Clone and cache a raw VarnodeData

  PcodeRawOutHelper(Translate &trans) {
    OpBehavior::registerInstructions(inst,&trans);
  }
  void clearCache(void);
  virtual void dump(const Address &addr,OpCode opc,VarnodeData *outvar,VarnodeData *vars,int4 isize);
};

/// Create an internal copy of the VarnodeData and cache it.
/// param var is the incoming VarnodeData being dumped
/// return the cloned VarnodeData
VarnodeData *PcodeRawOutHelper::createVarnode(const VarnodeData *var)
{
  VarnodeData *res = new VarnodeData();
  *res = *var;
  varcache.push_back(res);
  return res;
}

void PcodeRawOutHelper::clearCache(void)
{
  for(int4 i=0;i<opcache.size();++i)
    delete opcache[i];
  for(int4 i=0;i<varcache.size();++i)
    delete varcache[i];
  opcache.clear();
  varcache.clear();
}

void PcodeRawOutHelper::dump(const Address &addr,OpCode opc,VarnodeData *outvar,VarnodeData *vars,int4 isize)

{
  PcodeOpRaw *op = new PcodeOpRaw();
  op->setSeqNum(addr,uniq);
  opcache.push_back(op);
  op->setBehavior( inst[opc] );
  uniq += 1;
  if (outvar != (VarnodeData *)0) {
    VarnodeData *outvn = createVarnode(outvar);
    op->setOutput(outvn);
  }
  for(int4 i=0;i<isize;++i) {
    VarnodeData *invn = createVarnode(vars+i);
    op->addInput(invn);
  }
}
''')
log.debug('Ok')

class AssemblyEmitCacher(cppyy.gbl.AssemblyEmit):
  def dump(self, addr, mnem, body):
    self.addr = addr
    self.mnem = mnem
    self.body = body

# Import names into this namespace
from cppyy.gbl import Address
from cppyy.gbl import ContextInternal
from cppyy.gbl import DocumentStorage
from cppyy.gbl import get_opname
from cppyy.gbl import PcodeRawOutHelper
from cppyy.gbl import SimpleLoadImage
from cppyy.gbl import Sleigh
