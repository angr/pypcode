#ifndef PYPCODE_NATIVE_H
#define PYPCODE_NATIVE_H

#include "sleigh/loadimage.hh"
#include "sleigh/sleigh.hh"

// This is a tiny LoadImage class which feeds the executable bytes to the translator
class SimpleLoadImage : public LoadImage {
  uintb baseaddr;
  int4 length;
  uint1 *data;
public:
  SimpleLoadImage(uintb ad,uint1 *ptr,int4 sz) : LoadImage("nofile") { baseaddr = ad; data = ptr; length = sz; }
  void setData(uintb ad,uint1 *ptr,int4 sz) { baseaddr = ad; data = ptr; length = sz; }
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


  // FIXME: Lifetime of PcodeRawOutHelper is handled on Python side, but need
  // to add destructor to cleanup opcache/varcache on delete.
};

class AssemblyEmitCacher : public AssemblyEmit {
public:
  Address addr;
  string mnem;
  string body;

  void dump(const Address &addr,const string &mnem,const string &body) {
    this->addr = addr;
    this->mnem = mnem;
    this->body = body;
  };
};

#endif
