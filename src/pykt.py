import kyototycoon

max_ts = kyototycoon.DB.ll_max()

KTException = kyototycoon.Error

class Cursor:
	def __init__(self, cursor):
		self.cursor = cursor

	def set_value(self, value, expire=max_ts, step=False):
		return self.cursor.set_value(value, expire, step)

	def jump(self, key=''):
		v = self.cursor.jump(key)
		if not v:
			raise self.error()
		return v

	def jump_back(self, key=''):
		v = self.cursor.jump_back(key)
		if not v:
			raise self.error()
		return v

	def get(self, step=False):
		return self.cursor.get(step)

	def get_key(self, step=False):
		return self.cursor.get_key(step)

	def get_value(self, step=False):
		return self.cursor.get_value(step)

	def step(self):
		return self.cursor.step()

	def remove(self):
		v = self.cursor.remove()
		if not v:
			raise self.error()
		return v

	def error(self):
		return self.cursor.error()

class KyotoTycoon(kyototycoon.DB):
	'''
		pykt compatibility wrapper
	'''
	def __init__(self, *args, **kwargs):
		super(KyotoTycoon, self).__init__(*args, **kwargs)
		self.is_opened = False

	def check_is_opened(self):
		if not self.is_opened:
			raise IOError('you have to open the database first')

	def check_error(self):
		if self.error().code():
			raise self.error()

	def open(self, *args, **kwargs):
		if super(KyotoTycoon, self).open(*args, **kwargs):
			self.is_opened = True
			return self
		else:
			raise IOError('failed to open database.')

	def get(self, *args, **kwargs):
		self.check_is_opened()
		try:
			v = super(KyotoTycoon, self).get(*args, **kwargs)
		except kyototycoon.Error, e:
			if e.code() == 3 and 'no record' in e.message():
				return None
			raise e
		return v

	def add(self, key, value, expire=max_ts):
		self.check_is_opened()
		v = super(KyotoTycoon, self).add(key, value, expire)
		self.check_error()
		return v

	def append(self, key, value, expire=max_ts):
		self.check_is_opened()
		v = super(KyotoTycoon, self).append(key, value, expire)
		self.check_error()
		return v

	def set(self, key, value, expire=max_ts):
		self.check_is_opened()
		v = super(KyotoTycoon, self).set(key, value, expire)
		if not v:
			self.check_error()
		return v

	def cas(self, key, oval='', nval='', expire=max_ts):
		self.check_is_opened()
		v = super(KyotoTycoon, self).cas(key, oval, nval, expire)
		self.check_error()
		return v

	def clear(self):
		self.check_is_opened()
		v = super(KyotoTycoon, self).clear()
		if not v:
			self.check_error()
		return v

	def set_bulk(self, recs, expire=max_ts, atomic=True):
		self.check_is_opened()
		v = super(KyotoTycoon, self).set_bulk(recs, expire, atomic)
		if not v:
			self.check_error()
		return v

	def get_bulk(self, keys, atomic=True):
		self.check_is_opened()
		v = super(KyotoTycoon, self).get_bulk(keys, atomic)
		self.check_error()
		return v

	def increment(self, key, num=1, orig=0, expire=max_ts):
		self.check_is_opened()
		v = super(KyotoTycoon, self).increment(key, num, orig, expire)
		self.check_error()
		return v

	def increment_double(self, key, num=1.0, orig=0.0, expire=max_ts):
		self.check_is_opened()
		v = super(KyotoTycoon, self).increment_double(key, num, orig, expire)
		self.check_error()
		return v

	def match_prefix(self, prefix, max=-1):
		self.check_is_opened()
		v = super(KyotoTycoon, self).match_prefix(prefix, max)
		self.check_error()
		return v

	def remove(self, key):
		self.check_is_opened()
		v = super(KyotoTycoon, self).remove(key)
		#self.check_error() #It's not clear to me, when the return value and when an exception should be used
		return v

	def remove_bulk(self, keys, atomic=True):
		self.check_is_opened()
		v = super(KyotoTycoon, self).remove_bulk(keys, atomic)
		self.check_error()
		return v

	def set_bulk(self, recs, expire=max_ts, atomic=True):
		self.check_is_opened()
		v = super(KyotoTycoon, self).set_bulk(recs, expire, atomic)
		self.check_error()
		return v

	def replace(self, key, value, expire=max_ts):
		self.check_is_opened()
		v = super(KyotoTycoon, self).replace(key, value, expire)
		if not v:
			self.check_error()
		return v

	def report(self):
		self.check_is_opened()
		return super(KyotoTycoon, self).report()

	def status(self):
		self.check_is_opened()
		return super(KyotoTycoon, self).status()

	def cursor(self):
		return Cursor( super(KyotoTycoon, self).cursor() )

#db = KyotoTycoon("test").open()
#print db.report()