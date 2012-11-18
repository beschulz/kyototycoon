#
# This file is part of the Songbird web player.
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
#

# The purpose of this file is beeing able to generate the docs without having to install the module.


INCLUDE_DIRS = -I/usr/include/python2.7 -I/usr/include/c++
CXXFLAGS = -m64 -g -O3 -Wall -fPIC -fsigned-char -g0 -O2 -Os
LIBS = -lkyototycoon -lkyotocabinet -lpython -lstdc++
#-I/usr/local/include \
#-I/usr/include

help:
	@echo make help
	@echo make all
	@echo make doc
	@echo make unittests
	

#-D__x86_64__ -D__DARWIN_ALIAS_C 
./src/documentation.i : ./doc/generate_swig_doc.py ./doc/rpc_doc.txt
	cd doc; python generate_swig_doc.py

./src/kyototycoon_wrap.cpp: ./src/kyototycoon.i ./src/documentation.i ./src/documentation_manual.i ./src/wrapper.cpp ./src/wrapper.hpp
	swig -c++ -python -keyword -w511 -o ./src/kyototycoon_wrap.cpp ./src/kyototycoon.i
	#-lkyototycoon -lkyotocabinet  -lkyototycoon
	#-Wno-bool-conversions -Wno-c++11-narrowing -std=c++11 -stdlib=libc++
	
_kyototycoon.so: ./src/kyototycoon_wrap.cpp ./src/wrapper.cpp ./src/wrapper.hpp
	gcc ${CXXFLAGS} ${INCLUDE_DIRS} ./src/kyototycoon_wrap.cpp ./src/wrapper.cpp ${LIBS} -shared -o _kyototycoon.so

kyototycoon.py: ./src/kyototycoon.py
	cp ./src/kyototycoon.py .

doc: _kyototycoon.so kyototycoon.py
	cd doc; make html

all: _kyototycoon.so doc

unittests:
	source ./tests/.env/bin/activate
	nosetests tests

clean:
	rm -f *.cxx
	rm -f _kyototycoon.so
	rm -f *.pyc
	rm -f ./src/kyototycoon_wrap.cpp
	rm -f ./src/kyototycoon.py
	cd doc; make clean
	rm -Rf build
