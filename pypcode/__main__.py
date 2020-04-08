#!/usr/bin/env python
import argparse
from XbSymbolDatabase import XbSymbolScan

def main():
	p = argparse.ArgumentParser()
	p.add_argument('xbefile')
	args = p.parse_args()

	with open(args.xbefile, 'rb') as f:
		xbe = f.read()
		for lib, flags, sym, addr, ver in XbSymbolScan(xbe):
			print('%8s %4d %4x %08x %s' % (
				str(lib, encoding='ascii'), ver, flags, addr,
				str(sym, encoding='ascii')))

if __name__ == '__main__':
	main()
