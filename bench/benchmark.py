# -*- coding: utf-8 -*-
#from pykt import *
from pykt import KyotoTycoon as kt1
from kyototycoon import DB as kt2
from pykt_emu import KyotoTycoon as kt3
import timeit
from cPickle import dumps, loads

key = "A" * 12
val = "B" * 1024  

def bench_set(Impl):
	db = Impl()
	db.open()
	ret = db.set(key, val)
	assert ret == True
	db.close()

pykt_set  = lambda : bench_set(kt1)
kyoto_set = lambda : bench_set(kt2)

def bench_get(Impl):
	db = Impl()
	db.open()
	ret = db.get(key)
	assert ret == val
	db.close()

pykt_get  = lambda:bench_get(kt1)
kyoto_get = lambda:bench_get(kt2)

def bench_gets(Impl):
	db = Impl()
	db.open()
	
	for i in xrange(10):
		ret = db.get(key)
		assert ret == val
	db.close()

pykt_gets  = lambda:bench_gets(kt1)
kyoto_gets = lambda:bench_gets(kt2)

def bench_increment(Impl):
	db = Impl()
	db.open()
	ret = db.increment("N", 1)
	db.close()

pykt_increment  = lambda : bench_increment(kt1)
kyoto_increment = lambda : bench_increment(kt2)

def bench_replace(Impl):
	db = Impl()
	db.open()
	ret = db.replace(key, val)
	assert ret == True
	db.close()

pykt_replace  = lambda : bench_replace(kt1)
kyoto_replace = lambda : bench_replace(kt2)

def bench_append(Impl):
	db = Impl()
	db.open()
	ret = db.append(key, val)
	assert ret == True
	db.close()

pykt_append  = bench_append(kt1)
kyoto_append = bench_append(kt3)

implementations = (
	('pykt'        , kt1),
	('kyototycoon' , kt2),
	('pykt emu'    , kt3),
)

ops = (
	('set'      , bench_set),
	('get'      , bench_get),
	('gets'     , bench_gets),
	('increment', bench_increment),
	('replace'  , bench_replace),
	#('append'   , bench_append),
)

if __name__ == "__main__":
	print ' '*16 + '\t'.join(map(lambda x: '%15s' % (x[0]), ops)) + '	          total'
	for impl_name, impl in implementations:
		db=impl()
		db.open()
		db.clear()
		print '%15s' % (impl_name),
		total = 0.0
		for op_name, op in ops:
			bound = lambda:op(impl)
			t = timeit.Timer(bound)
			bound()#warmup
			#t.timeit(number=100)#warmup
			res = t.timeit(number=1000)
			total += res
			print '%2.13f'%(res),
		print '%2.13f'%(total)

	'''
	res = timeit.timeit("pykt_set()", "from __main__ import pykt_set", number=1000)
	print "pykt_set %f" % res
	#res = timeit.timeit("pykt_replace()", "from __main__ import pykt_replace", number=1000)
	#print "pykt_replace %f" % res
	res = timeit.timeit("kyoto_set()", "from __main__ import kyoto_set", number=1000)
	print "kt_set %f" % res
	
	#res = timeit.timeit("pykt_append()", "from __main__ import pykt_append", number=1000)
	#print "pykt_append %f" % res
	#res = timeit.timeit("kyoto_append()", "from __main__ import kyoto_append", number=1000)
	#print "kt_append %f" % res
	
	res = timeit.timeit("pykt_get()", "from __main__ import pykt_get", number=1000)
	print "pykt_get %f" % res
	res = timeit.timeit("kyoto_get()", "from __main__ import kyoto_get", number=1000)
	print "kt_get %f" % res

	res = timeit.timeit("pykt_gets()", "from __main__ import pykt_gets", number=100)
	print "pykt_gets %f" % res
	res = timeit.timeit("kyoto_gets()", "from __main__ import kyoto_gets", number=100)
	print "kt_gets %f" % res

	res = timeit.timeit("pykt_increment()", "from __main__ import pykt_increment", number=1000)
	print "pykt_increment %f" % res
	res = timeit.timeit("kyoto_increment()", "from __main__ import kyoto_increment", number=1000)
	print "kt_increment %f" % res
	'''

