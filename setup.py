#!/usr/bin/env python3
import os
from setuptools import setup, find_packages
from wheel.bdist_wheel import bdist_wheel
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


class bdist_wheel_abi3(bdist_wheel):
    def get_tag(self):
        python, abi, plat = super().get_tag()

        if python.startswith("cp"):
            # on CPython, our wheels are abi3 and compatible back to 3.8
            return "cp38", "abi3", plat

        return python, abi, plat


setup(name='pypcode',
      version='1.1.0',
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
      cmdclass=dict(build_ext=build_cffi.FfiPreBuildExtension,
                    bdist_wheel=bdist_wheel_abi3),
      python_requires='>=3.8'
      )
