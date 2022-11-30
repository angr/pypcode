#!/usr/bin/env python3
import os
import sys

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(ROOT_DIR)

from setuptools import setup
import build_cffi


with open(os.path.join(ROOT_DIR, 'README.md')) as f:
    long_description = f.read()


def add_pkg_data_dirs(pkg, dirs):
       pkg_data = []
       for d in dirs:
               for root, _, files in os.walk(os.path.join(pkg, d)):
                       r = os.path.relpath(root, pkg)
                       pkg_data.extend([os.path.join(r, f) for f in files])
       return pkg_data


cmdclass = {
    'build_ext': build_cffi.FfiPreBuildExtension
}

try:
    from wheel.bdist_wheel import bdist_wheel
    class bdist_wheel_abi3(bdist_wheel):
        def get_tag(self):
            python, abi, plat = super().get_tag()
            if python.startswith("cp"):
                return "cp38", "abi3", plat
            return python, abi, plat
    cmdclass['bdist_wheel'] = bdist_wheel_abi3
except ImportError:
    pass


setup(name='pypcode',
      version='1.1.1',
      description="Python bindings to Ghidra's SLEIGH library",
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
      cmdclass=cmdclass,
      python_requires='>=3.8',
      )
