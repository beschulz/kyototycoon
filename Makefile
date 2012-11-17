INCLUDE_DIRS = -I/usr/include/python2.7 -I/usr/include/c++
CXXFLAGS = -m64 -g -O3 -Wall -fPIC -fsigned-char -g0 -O2 -Os
LIBS = -lkyototycoon -lkyotocabinet -lpython -lstdc++
#-I/usr/local/include \
#-I/usr/include

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
