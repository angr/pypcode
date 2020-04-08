#!/usr/bin/env python
#
# Based on sleighexample.cc
#
# First: pip install cppyy
#

import cppyy
import sys
import logging
import os.path

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s] %(levelname)s: %(message)s')
log = logging.getLogger(__name__)

PYPCODENATIVE_PATH=os.path.join(os.path.dirname(__file__), 'pypcode-native')
SLEIGH_PATH=os.path.join(PYPCODENATIVE_PATH, 'sleigh-2.1.0')
SLEIGH_SRC_PATH=os.path.join(SLEIGH_PATH, 'src')
SLEIGH_SPECFILES_PATH=os.path.join(SLEIGH_PATH, 'specfiles')

log.debug('Loading Headers')
cppyy.include(os.path.join(SLEIGH_SRC_PATH, 'loadimage.hh'))
cppyy.include(os.path.join(SLEIGH_SRC_PATH, 'sleigh.hh'))
cppyy.include(os.path.join(SLEIGH_SRC_PATH, 'emulate.hh'))

log.debug('Loading Library')
cppyy.load_library(os.path.join(PYPCODENATIVE_PATH, 'pypcode-native.so'))

log.debug('Creating Loader')
cppyy.cppdef('''
void test_me(string &action);

// This is a tiny LoadImage class which feeds the executable bytes to the translator
class MyLoadImage : public LoadImage {
  uintb baseaddr;
  int4 length;
  uint1 *data;
public:
  MyLoadImage(uintb ad,uint1 *ptr,int4 sz) : LoadImage("nofile") { baseaddr = ad; data = ptr; length = sz; }
  virtual void loadFill(uint1 *ptr,int4 size,const Address &addr);
  virtual string getArchType(void) const { return "myload"; }
  virtual void adjustVma(long adjust) { }
};

// This is the only important method for the LoadImage. It returns bytes from the static array
// depending on the address range requested
void MyLoadImage::loadFill(uint1 *ptr,int4 size,const Address &addr)

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

log.debug('Creating Emulation class')
cppyy.cppdef('''
// -------------------------------------
//
// These are the classes/routines relevant for emulating the executable

// A simple class for emulating the system "puts" call.
// It justs looks up the string data and dumps it to standard out.
class PutsCallBack : public BreakCallBack {
public:
  virtual bool addressCallback(const Address &addr);
};

bool PutsCallBack::addressCallback(const Address &addr)

{
  MemoryState *mem = static_cast<EmulateMemory *>(emulate)->getMemoryState();
  uint1 buffer[256];
  uint4 esp = mem->getValue("ESP");
  AddrSpace *ram = mem->getTranslate()->getSpaceByName("ram");

  uint4 param1 = mem->getValue(ram,esp+4,4);
  mem->getChunk(buffer,ram,param1,255);

  cout << (char *)&buffer << endl;

  uint4 returnaddr = mem->getValue(ram,esp,4);
  mem->setValue("ESP",esp+8);
  emulate->setExecuteAddress(Address(ram,returnaddr));
  
  return true;      // This replaces the indicated instruction
}

#if 0
// A simple class for emulating the system "printf" call.
// We don't really emulate all of it.  The only printf call in the example
// has an initial string of "%d\n". So we grab the second parameter from the
// memory state and print it as an integer
#endif
class PrintfCallBack : public BreakCallBack {
public:
  virtual bool addressCallback(const Address &addr);
};

bool PrintfCallBack::addressCallback(const Address &addr)

{
  MemoryState *mem = static_cast<EmulateMemory *>(emulate)->getMemoryState();

  AddrSpace *ram = mem->getTranslate()->getSpaceByName("ram");

  uint4 esp = mem->getValue("ESP");
  uint4 param2 = mem->getValue(ram,esp+8,4);
  cout << (int4)param2 << endl;

  uint4 returnaddr = mem->getValue(ram,esp,4);
  mem->setValue("ESP",esp+12);
  emulate->setExecuteAddress(Address(ram,returnaddr));

  return true;
}

// A callback that terminates the emulation
class TerminateCallBack : public BreakCallBack {
public:
  virtual bool addressCallback(const Address &addr);
};

bool TerminateCallBack::addressCallback(const Address &addr)

{
  emulate->setHalt(true);

  return true;
}

static void doEmulation(Translate &trans,LoadImage &loader)

{
  // Set up memory state object
  MemoryImage loadmemory(trans.getDefaultSpace(),8,4096,&loader);
  MemoryPageOverlay ramstate(trans.getDefaultSpace(),8,4096,&loadmemory);
  MemoryHashOverlay registerstate(trans.getSpaceByName("register"),8,4096,4096,(MemoryBank *)0);
  MemoryHashOverlay tmpstate(trans.getUniqueSpace(),8,4096,4096,(MemoryBank *)0);

  MemoryState memstate(&trans); // Instantiate the memory state object
  memstate.setMemoryBank(&ramstate);
  memstate.setMemoryBank(&registerstate);
  memstate.setMemoryBank(&tmpstate);

  BreakTableCallBack breaktable(&trans); // Set up the callback object
  EmulatePcodeCache emulater(&trans,&memstate,&breaktable); // Set up the emulator

  // Set up the initial register state for execution
  memstate.setValue("ESP",0xbffffffc);
  emulater.setExecuteAddress(Address(trans.getDefaultSpace(),0x80483b4));

  // Register callbacks
  PutsCallBack putscallback;
  PrintfCallBack printfcallback;
  TerminateCallBack terminatecallback;
  breaktable.registerAddressCallback(Address(trans.getDefaultSpace(),0x80482c8),&putscallback);
  breaktable.registerAddressCallback(Address(trans.getDefaultSpace(),0x80482b8),&printfcallback);
  breaktable.registerAddressCallback(Address(trans.getDefaultSpace(),0x804846b),&terminatecallback);

  emulater.setHalt(false);

  do {
    emulater.executeInstruction();
  } while(!emulater.getHalt());
}

''')

# These are the bytes for an example x86 binary
# These bytes are loaded at address 0x80483b4
myprog = bytearray([
  0x8d, 0x4c, 0x24, 0x04, 0x83, 0xe4, 0xf0, 0xff, 0x71, 0xfc, 0x55,
  0x89, 0xe5, 0x51, 0x81, 0xec, 0xb4, 0x01, 0x00, 0x00, 0xc7, 0x45, 0xf4,
  0x00, 0x00, 0x00, 0x00, 0xeb, 0x12, 0x8b, 0x45, 0xf4, 0xc7, 0x84,
  0x85, 0x64, 0xfe, 0xff, 0xff, 0x00, 0x00, 0x00, 0x00, 0x83, 0x45, 0xf4,
  0x01, 0x83, 0x7d, 0xf4, 0x63, 0x7e, 0xe8, 0xc7, 0x45, 0xf4, 0x02,
  0x00, 0x00, 0x00, 0xeb, 0x28, 0x8b, 0x45, 0xf4, 0x01, 0xc0, 0x89, 0x45,
  0xf8, 0xeb, 0x14, 0x8b, 0x45, 0xf8, 0xc7, 0x84, 0x85, 0x64, 0xfe,
  0xff, 0xff, 0x01, 0x00, 0x00, 0x00, 0x8b, 0x45, 0xf4, 0x01, 0x45, 0xf8,
  0x83, 0x7d, 0xf8, 0x63, 0x7e, 0xe6, 0x83, 0x45, 0xf4, 0x01, 0x83,
  0x7d, 0xf4, 0x31, 0x7e, 0xd2, 0xc7, 0x04, 0x24, 0x40, 0x85, 0x04, 0x08,
  0xe8, 0x9c, 0xfe, 0xff, 0xff, 0xc7, 0x45, 0xf4, 0x02, 0x00, 0x00,
  0x00, 0xeb, 0x25, 0x8b, 0x45, 0xf4, 0x8b, 0x84, 0x85, 0x64, 0xfe, 0xff,
  0xff, 0x85, 0xc0, 0x75, 0x13, 0x8b, 0x45, 0xf4, 0x89, 0x44, 0x24,
  0x04, 0xc7, 0x04, 0x24, 0x47, 0x85, 0x04, 0x08, 0xe8, 0x62, 0xfe, 0xff,
  0xff, 0x83, 0x45, 0xf4, 0x01, 0x83, 0x7d, 0xf4, 0x63, 0x7e, 0xd5,
  0x81, 0xc4, 0xb4, 0x01, 0x00, 0x00, 0x59, 0x5d, 0x8d, 0x61, 0xfc, 0xc3,
  0x90, 0x90, 0x90, 0x90, 0x55, 0x89, 0xe5, 0x5d, 0xc3, 0x8d, 0x74,
  0x26, 0x00, 0x8d, 0xbc, 0x27, 0x00, 0x00, 0x00, 0x00, 0x55, 0x89, 0xe5,
  0x57, 0x56, 0x53, 0xe8, 0x5e, 0x00, 0x00, 0x00, 0x81, 0xc3, 0xa5,
  0x11, 0x00, 0x00, 0x83, 0xec, 0x1c, 0xe8, 0xd7, 0xfd, 0xff, 0xff, 0x8d,
  0x83, 0x20, 0xff, 0xff, 0xff, 0x89, 0x45, 0xf0, 0x8d, 0x83, 0x20,
  0xff, 0xff, 0xff, 0x29, 0x45, 0xf0, 0xc1, 0x7d, 0xf0, 0x02, 0x8b, 0x55,
  0xf0, 0x85, 0xd2, 0x74, 0x2b, 0x31, 0xff, 0x89, 0xc6, 0x8d, 0xb6,
  0x00, 0x00, 0x00, 0x00, 0x8b, 0x45, 0x10, 0x83, 0xc7, 0x01, 0x89, 0x44,
  0x24, 0x08, 0x8b, 0x45, 0x0c, 0x89, 0x44, 0x24, 0x04, 0x8b, 0x45,
  0x08, 0x89, 0x04, 0x24, 0xff, 0x16, 0x83, 0xc6, 0x04, 0x39, 0x7d, 0xf0,
  0x75, 0xdf, 0x83, 0xc4, 0x1c, 0x5b, 0x5e, 0x5f, 0x5d, 0xc3, 0x8b,
  0x1c, 0x24, 0xc3, 0x90, 0x90, 0x90, 0x55, 0x89, 0xe5, 0x53, 0xbb, 0x50,
  0x95, 0x04, 0x08, 0x83, 0xec, 0x04, 0xa1, 0x50, 0x95, 0x04, 0x08,
  0x83, 0xf8, 0xff, 0x74, 0x0c, 0x83, 0xeb, 0x04, 0xff, 0xd0, 0x8b, 0x03,
  0x83, 0xf8, 0xff, 0x75, 0xf4, 0x83, 0xc4, 0x04, 0x5b, 0x5d, 0xc3,
  0x55, 0x89, 0xe5, 0x53, 0x83, 0xec, 0x04, 0xe8, 0x00, 0x00, 0x00, 0x00,
  0x5b, 0x81, 0xc3, 0x0c, 0x11, 0x00, 0x00, 0xe8, 0x00, 0xfe, 0xff,
  0xff, 0x59, 0x5b, 0xc9, 0xc3, 0x03, 0x00, 0x00, 0x00, 0x01, 0x00, 0x02,
  0x00, 0x00, 0x00, 0x00, 0x00, 0x50, 0x72, 0x69, 0x6d, 0x65, 0x73,
  0x00, 0x25, 0x64, 0x0a, 0x00, 0x00
  ])

#
# Define a helper class that recieves pcode ops from the translator and caches
# them in member variables to be accessed from Python side
#
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

class PythonAssemblyRaw(cppyy.gbl.AssemblyEmit):
  def dump(self, addr, mnem, body):
    sys.stdout.write('%08x: %s %s\n' % (addr.getOffset(), mnem, body))

#
# FIXME: Check memory locations. Seems to be writing to random locations (ASLR?)
#

def dumpPcode(trans):
  """
  Dump pcode translation of machine instructions
  """
  log.debug('Dumping pcode')

  def print_vardata(data):
    sys.stdout.write('(%s, 0x%x, %d) ' % (data.space.getName(), data.offset, data.size))
    if data.space.getName() == 'register':
      regname = trans.getRegisterName(data.space, data.offset, data.size)
      sys.stdout.write('{%s} ' % regname)

  emit = cppyy.gbl.PcodeRawOutHelper(trans) # Set up the pcode dumper
  # assememit = cppyy.gbl.AssemblyRaw() # Set up the disassembly dumper
  assememit = PythonAssemblyRaw() # Set up the disassembly dumper

  addr = cppyy.gbl.Address(trans.getDefaultSpace(), 0x80483b4) # First address to translate
  lastaddr = cppyy.gbl.Address(trans.getDefaultSpace(), 0x80483bf) # Last address

  while addr < lastaddr:
    emit.clearCache()
    trans.printAssembly(assememit, addr)
    length = trans.oneInstruction(emit, addr) # Translate instruction
    # import ipdb; ipdb.set_trace()
    
    # Print output
    for op in emit.opcache:
      out = op.getOutput()
      if out:
        print_vardata(out)
        sys.stdout.write('= ')
      sys.stdout.write('%s ' % cppyy.gbl.get_opname(op.getOpcode()))
      for i in range(op.numInput()):
        print_vardata(op.getInput(i))
      sys.stdout.write('\n')

    sys.stdout.write('\n')
    addr = addr + length # Advance to next instruction
    
def dumpAssembly(trans):
  assememit = PythonAssemblyRaw() # Set up the disassembly dumper

  addr = cppyy.gbl.Address(trans.getDefaultSpace(), 0x80483b4) # First address to translate
  lastaddr = cppyy.gbl.Address(trans.getDefaultSpace(), 0x80483bf) # Last address

  while addr < lastaddr:
    length = trans.printAssembly(assememit, addr)
    addr = addr + length # Advance to next instruction
    