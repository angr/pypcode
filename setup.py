#!/usr/bin/env python
import os
import os.path
import platform
import shutil
import subprocess
from setuptools import setup
from setuptools.command.build_py import build_py
import struct

is_64b = (struct.calcsize("P")*8 == 64)

PKG_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_SRC_DIR = os.path.join(PKG_DIR, 'pypcode')
LIB_SRC_DIR = os.path.join(PKG_SRC_DIR, 'pypcode-native')
SPECFILES_DIR = os.path.join(PKG_SRC_DIR, 'processors')

BIN_EXTENSION = {
  'Windows' : '.exe',
  'Linux'   : '',
  'Darwin'  : ''
}[platform.system()]

# cffi:setuptools_ext.py
def execfile(filename, glob):
	# We use execfile() (here rewritten for Python 3) instead of
	# __import__() to load the build script.  The problem with
	# a normal import is that in some packages, the intermediate
	# __init__.py files may already try to import the file that
	# we are generating.
	with open(filename) as f:
		src = f.read()
	src += '\n'      # Python 2.6 compatibility
	code = compile(src, filename, 'exec')
	exec(code, glob, glob)

class custom_build(build_py):
	def run(self):
		try:
			out = subprocess.check_output(['cmake', '--version'])
		except OSError:
			raise RuntimeError('Please install CMake to build')

		cmake_config_args = [
			'-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON',
			'-DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE',
			]
		cmake_build_args = []
		if platform.system() == 'Windows':
			cmake_config_args += ['-A', 'x64' if is_64b else 'Win32']
			cmake_build_args += ['--config', 'Release']

		# Build sleigh and csleigh library
		SLEIGH_BUILD_DIR=os.path.join(LIB_SRC_DIR, 'build')
		subprocess.check_call(['cmake', '-S', '.', '-B', 'build'] + cmake_config_args, cwd=LIB_SRC_DIR)
		subprocess.check_call(['cmake', '--build', 'build', '--parallel', '--verbose'] + cmake_build_args, cwd=LIB_SRC_DIR)
		shutil.rmtree(SLEIGH_BUILD_DIR)

		# Build sla files
		sleigh = os.path.join(LIB_SRC_DIR, 'bin', 'sleigh' + BIN_EXTENSION)
		subprocess.check_call([sleigh, '-a', SPECFILES_DIR])

		# Build CFFI module
		build_file_name = 'pypcode/pypcode-native/cffi_build.py'
		mod_vars = {'__name__': '__main__', '__file__': build_file_name}
		execfile(build_file_name, mod_vars)

		return super().run()

with open('README.md') as f:
	long_description = f.read()

setup(name='pypcode',
	version='0.0.4',
	description='Python bindings to Ghidra\'s SLEIGH library',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='Matt Borgerson',
	author_email='contact@mborgerson.com',
	url='https://github.com/angr/pypcode',
	cmdclass=dict(build_py=custom_build),
	packages=['pypcode'],
	include_package_data=True,
	setup_requires=['cffi'],
	install_requires=['cffi']
	)
