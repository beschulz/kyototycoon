#!/usr/bin/env python
#
# This file is part of the kyototycoon SWIG binding.
#
# Copyright(c) Benjamin Schulz (beschulz[the a with the stuff]betabugs.de)
# https://github.com/beschulz/kyototycoon
#
# This file may be licensed under the terms of of the
# GNU General Public License Version 2 (the ``GPL'').
#
# Software distributed under the License is distributed
# on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
# express or implied. See the GPL for the specific language
# governing rights and limitations.
#
# You should have received a copy of the GPL along with this
# program. If not, go to http://www.gnu.org/licenses/gpl.html
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

#from distutils.core import setup, Extension
from setuptools import setup, Extension

import os
if os.uname()[0] == 'Darwin':
	# workaround for mac os x
	os.environ['ARCHFLAGS'] = "-arch x86_64"

def read(name):
	return open(os.path.join(os.path.dirname(__file__), name)).read()

kyototycoon_module = Extension(
	'kyototycoon._kyototycoon', ['./kyototycoon/kyototycoon.i', './kyototycoon/wrapper.cpp'],
	swig_opts=['-c++', '-keyword', '-w511', '-dhtml'], #-w511 suppresses warning about swig not being able to use keyword arguments for some internal stuff
	libraries=['kyototycoon', 'kyotocabinet'],
	extra_compile_args=['-m64', '-g', '-O3', '-Wall', '-fPIC'], #-m64, because we don't want 32-bit
)

setup (
	name = 'kyototycoon',
	version = '0.0.1',
	author      = "Benjamin Schulz",
	author_email='beschulz[the a with the weird stuff attatched to it]betabugs.de',
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
	packages = ['kyototycoon', 'pykt'],
	#package_dir = {'kyototycoon':'src', 'pykt' : 'lib/pykt'},
	setup_requires=['nose>=1.0', 'coverage', 'sphinx'],
)
