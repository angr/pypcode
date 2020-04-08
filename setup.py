#!/usr/bin/env python
import os
import os.path
import platform
import shutil
import subprocess
from setuptools import setup
from setuptools.command.build_py import build_py

SOURCE_DIR = os.path.abspath(os.path.dirname(__file__))
LIB_SOURCE_DIR = os.path.join(SOURCE_DIR, 'pypcode', 'pypcode-native')
OUTPUT_DIR = os.path.join(SOURCE_DIR, 'pypcode')

class custom_build(build_py):
	def run(self):
		if not os.path.exists(OUTPUT_DIR):
			os.makedirs(OUTPUT_DIR)
		subprocess.check_call(['make'], cwd=LIB_SOURCE_DIR)
		shutil.copyfile(os.path.join(LIB_SOURCE_DIR, 'pypcode-native.so'),
		                os.path.join(OUTPUT_DIR,     'pypcode-native.so'))
		return super().run()

with open('README.md') as f:
	long_description = f.read()

setup(name='pypcode',
	version='0.0.1',
	description='Python bindings to Ghidra\'s SLEIGH library',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='Matt Borgerson',
	author_email='contact@mborgerson.com',
	url='https://github.com/mborgerson/pypcode',
	license='GPL',
	cmdclass=dict(build_py=custom_build),
	include_package_data=True,
	packages=['pypcode'],
	package_data={
		'pypcode': ['pypcode-native.*']
		}
	)
