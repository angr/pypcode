#!/bin/bash
# Use this to rebuild the module if you have installed the package
# in editable mode
set -e
set -x
cmake -S . -B build && cmake --build build --parallel --verbose
python cffi_build.py && mv pypcode/_csleigh*.so ..
