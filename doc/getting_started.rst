Getting started
=======================================

Installation
==================

.. code:: bash

	# get latest source for kyoto cabinet from fallabs and compile it:
	wget http://fallabs.com/kyotocabinet/pkg/kyotocabinet-<version-number>.tar.gz
	tar -xvf kyotocabinet-<version-number>.tar.gz
	cd kyotocabinet-<version-number>
	./configure
	make all
	make install

	# get latest source for kyoto tycoon from fallabs and compile it:
	wget http://fallabs.com/kyototycoon/pkg/kyototycoon-<version-number.tar.gz
	tar -xvf kyototycoon-<version-number.tar.gz
	cd kyototycoon-<version-number
	./configure
	make all
	make install

	#compile the module itself:
	git clone git://github.com/beschulz/kyototycoon.git
	cd kyototycoon
	python setup.py install

	# (optional, but highly recommended) run the tests
	pip install nose
	nosetests tests

	# (optional) build documentation
	pip install Sphinx
	make docs
