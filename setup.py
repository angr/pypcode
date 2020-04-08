#!/usr/bin/env python
import os
import os.path
import platform
import shutil
import subprocess
from setuptools import setup
from setuptools.command.build_py import build_py

SOURCE_DIR = os.path.abspath(os.path.dirname(__file__))
LIB_SOURCE_DIR = os.path.join(SOURCE_DIR, 'XbSymbolDatabase', 'XbSymbolDatabase')
OUTPUT_DIR = os.path.join(SOURCE_DIR, 'XbSymbolDatabase')

class custom_build(build_py):
	def run(self):
		try:
			out = subprocess.check_output(['cmake', '--version'])
		except OSError:
			raise RuntimeError('Please install CMake to build')

		cmake_args = [
			'-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + OUTPUT_DIR,
			'-DBUILD_SHARED_LIBS=ON'
			]
		if not os.path.exists(OUTPUT_DIR):
			os.makedirs(OUTPUT_DIR)
		subprocess.check_call(['cmake', '.'] + cmake_args, cwd=LIB_SOURCE_DIR)
		subprocess.check_call(['cmake', '--build', '.'], cwd=LIB_SOURCE_DIR)

		# Windows does things a little differently...
		if platform.system() == 'Windows':
			src = os.path.join(LIB_SOURCE_DIR, 'Debug', 'XbSymbolDatabase.dll')
			dest = os.path.join(OUTPUT_DIR, 'libXbSymbolDatabase.dll')
			shutil.copyfile(src, dest)

		return super().run()

with open('README.md') as f:
	long_description = f.read()

setup(name='PyXbSymbolDatabase',
	version='0.0.1',
	description='Python bindings to XbSymbolDatabase',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='Matt Borgerson',
	author_email='contact@mborgerson.com',
	url='https://github.com/mborgerson/PyXbSymbolDatabase',
	license='GPL',
	cmdclass=dict(build_py=custom_build),
	include_package_data=True,
	packages=['XbSymbolDatabase'],
	package_data={
		'XbSymbolDatabase': ['libXbSymbolDatabase.*']
		}
	)
