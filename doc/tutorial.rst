Tutorial
=======================================

A quick example for the impatient
=======================================

.. code:: python

	import kyototycoon

	db = kyototycoon.DB()
	db.open()

	db.set_bulk( {'a':'1', 'b': '2', 'c' : '3', 'aaa' : '111'} )
	db.get('a')

	cur = db.cursor()
	cur.jump()

	cur.get()
	cur.step()
	cur.get()

	db.get('this one is not there')
	db.error()

	db.get_bulk(('a', 'b'))

	db.match_prefix('a')

	# you can use the db like a dictionary:
	db['foo'] = 'bar'
	assert( db['foo'] == 'bar')