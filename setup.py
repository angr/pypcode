#!/usr/bin/env python3
from setuptools import setup, find_packages
from build_cffi import FfiPreBuildExtension
import os, os.path

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
	version='1.0.2',
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
	cmdclass={'build_ext': FfiPreBuildExtension},
	python_requires='>=3.6'
	)
