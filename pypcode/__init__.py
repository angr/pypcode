#!/usr/bin/env python
import ctypes
import os.path
import platform

libname = 'libXbSymbolDatabase'

# Determine shared library file extension
osname = platform.system()
if osname == 'Linux':
	libname += '.so'
elif osname == 'Darwin':
	libname += '.dylib'
elif osname == 'Windows':
	libname += '.dll'
else:
	assert(False), "Unknown platform"

libpath = os.path.join(os.path.dirname(__file__), libname)
lib = ctypes.cdll.LoadLibrary(libpath)

def XbSymbolScan(xbe):
	assert(xbe[0:4] == b'XBEH'), 'Invalid XBE header'
	symbols = []
	cb_wrap = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_uint32, ctypes.c_char_p, ctypes.c_uint32, ctypes.c_uint32)
	def cb(library_str, library_flag, symbol_str, address, build_verison):
		symbols.append((library_str, library_flag, symbol_str, address, build_verison))
	lib.XbSymbolScan(xbe, cb_wrap(cb), True)
	return symbols
