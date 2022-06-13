#!/usr/bin/env python3
import os
from setuptools import setup, find_packages
import sys

sys.path.append(os.getcwd())
import build_cffi

def add_pkg_data_dirs(pkg, dirs):
	pkg_data = []
	for d in dirs:
		for root, _, files in os.walk(os.path.join(pkg, d)):
			r = os.path.relpath(root, pkg)
			pkg_data.extend([os.path.join(r, f) for f in files])
	return pkg_data

with open('README.md') as f:
	long_description = f.read()

setup(name='pypcode',
	version='1.0.6',
	description='Python bindings to Ghidra\'s SLEIGH library',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='Matt Borgerson',
	author_email='contact@mborgerson.com',
	url='https://github.com/angr/pypcode',
	packages=['pypcode'],
	package_data={'pypcode': add_pkg_data_dirs('pypcode', ['processors', 'docs'])},
	setup_requires=['cffi'],
	install_requires=['cffi'],
	cffi_modules=['build_cffi.py:ffibuilder'],
	cmdclass={'build_ext': build_cffi.FfiPreBuildExtension},
	python_requires='>=3.6'
	)
