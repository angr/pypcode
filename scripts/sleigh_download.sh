#!/bin/bash
set -e
set -x

git clone --depth=1 -b Ghidra_11.4.1_build https://github.com/NationalSecurityAgency/ghidra.git ghidra_src

# We just need Makefile and $(LIBSLA_SOURCE) defined inside Makefile. Do it this
# way to make sure we stay up to date with the list of required files.
SLEIGH_SRC_DIR=sleigh
pushd ghidra_src/Ghidra/Features/Decompiler/src/decompile/cpp/

# Touch fake dependency files recently removed upstream. Not having these triggers build steps.
mkdir -p com_opt com_dbg
touch com_opt/depend com_dbg/depend

echo -e "$SLEIGH_SRC_DIR:\n\tmkdir -p $SLEIGH_SRC_DIR\n\tcp \$(LIBSLA_SOURCE) Makefile $SLEIGH_SRC_DIR" >> Makefile
make $SLEIGH_SRC_DIR
SLEIGH_SRC_DIR=${PWD}/${SLEIGH_SRC_DIR}
popd

mv $SLEIGH_SRC_DIR .
mv ghidra_src/Ghidra/Processors processors
