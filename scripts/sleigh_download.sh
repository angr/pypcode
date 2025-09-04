#!/bin/bash
set -e
set -x

TAG=11.4.2
GHIDRA_SRC_DIR=ghidra_src_${TAG}
git clone --depth=1 -b Ghidra_${TAG}_build https://github.com/NationalSecurityAgency/ghidra.git ${GHIDRA_SRC_DIR}

# We just need Makefile and $(LIBSLA_SOURCE) defined inside Makefile. Do it this
# way to make sure we stay up to date with the list of required files.
SLEIGH_SRC_DIR=sleigh
pushd ${GHIDRA_SRC_DIR}/Ghidra/Features/Decompiler/src/decompile/cpp/

# Touch fake dependency files recently removed upstream. Not having these triggers build steps.
mkdir -p com_opt com_dbg
touch com_opt/depend com_dbg/depend

echo -e "$SLEIGH_SRC_DIR:\n\tmkdir -p $SLEIGH_SRC_DIR\n\tcp \$(LIBSLA_SOURCE) Makefile $SLEIGH_SRC_DIR" >> Makefile
make $SLEIGH_SRC_DIR
SLEIGH_SRC_DIR=${PWD}/${SLEIGH_SRC_DIR}
popd

mkdir ${TAG}
mv $SLEIGH_SRC_DIR ${TAG}
mv ${GHIDRA_SRC_DIR}/Ghidra/Processors ${TAG}/processors
