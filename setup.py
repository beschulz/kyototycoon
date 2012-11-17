#!/usr/bin/env python
"""
setup.py file for kyototycoon SWIG bindings
"""
from distutils.core import setup, Extension

import os
if os.uname()[0] == 'Darwin':
	os.environ['ARCHFLAGS'] = "-arch x86_64"

def read(name):
	return open(os.path.join(os.path.dirname(__file__), name)).read()

kyototycoon_module = Extension(
	'_kyototycoon', ['./src/kyototycoon.i', './src/wrapper.cpp'],
	swig_opts=['-c++', '-keyword', '-w511', '-dhtml'], #-w511 suppresses warning about swig not being able to use keyword arguments for some internal stuff
	libraries=['kyototycoon', 'kyotocabinet'],
	extra_compile_args=['-m64', '-g', '-O3', '-Wall', '-fPIC'], #-m64, because we don't want 32-bit
)

setup (
	name = 'kyototycoon',
	version = '0.0.1',
	author      = "Benjamin Schulz",
	author_email='beschulz[the a with the weird stuff attatched it]betabugs.de',
	url='https://github.com/beschulz/kyototycoon',
	license='GPL',
	#platforms=['Linux', 'Darwin', 'Windows'],
	test_suite = 'nose.collector',
	description = """SWIG bindings for kyototycoon's ktremotedb""",
	long_description=read("README.rst"),
	keywords='KyotoTycoon',
	classifiers=[
			"Intended Audience :: Developers",
			'License :: OSI Approved :: BSD License',
			'Operating System :: POSIX :: Linux',
			'Programming Language :: C',
			"Topic :: Database :: Front-Ends",
			"Topic :: Software Development :: Libraries"
	],
	ext_modules = [kyototycoon_module],
	py_modules = ["kyototycoon", "pykt"],
	package_dir = {'': 'src'},
)
