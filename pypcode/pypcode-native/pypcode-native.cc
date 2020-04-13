#include "pypcode-native.h"

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
