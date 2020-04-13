#ifndef PYPCODE_NATIVE_H
#define PYPCODE_NATIVE_H

#include "sleigh-2.1.0/src/loadimage.hh"
#include "sleigh-2.1.0/src/sleigh.hh"

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

#endif
