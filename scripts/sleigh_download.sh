#!/bin/bash
set -e
set -x

TAG=12.1.4
GHIDRA_SRC_DIR=ghidra_src_${TAG}
git clone --depth=1 -b Ghidra_${TAG}_build https://github.com/NationalSecurityAgency/ghidra.git ${GHIDRA_SRC_DIR}

# We just need Makefile and $(LIBSLA_SOURCE) defined inside Makefile. Do it this
# way to make sure we stay up to date with the list of required files.
#
# Only evaluate the variable; don't build anything. Ghidra ships the bison/flex
# generated sources checked in and does not regenerate them during its build, so
# copy them as-is. DEPNAMES= skips including the depend files, which would
# otherwise cause make to regenerate parsers depending on checkout timestamps.
SLEIGH_SRC_DIR=${PWD}/sleigh
pushd ${GHIDRA_SRC_DIR}/Ghidra/Features/Decompiler/src/decompile/cpp/
LIBSLA_SOURCE=$(make -s --no-print-directory -f Makefile -f - print-libsla-source DEPNAMES= <<'EOF'
print-libsla-source:
	@echo $(LIBSLA_SOURCE)
EOF
)
mkdir -p ${SLEIGH_SRC_DIR}
cp ${LIBSLA_SOURCE} Makefile ${SLEIGH_SRC_DIR}
popd

mkdir ${TAG}
mv $SLEIGH_SRC_DIR ${TAG}
mv ${GHIDRA_SRC_DIR}/Ghidra/Processors ${TAG}/processors
