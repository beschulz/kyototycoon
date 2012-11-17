of = open('../src/documentation.i', 'wt')

with open('rpc_doc.txt') as f:
	doc = []
	method = None
	for line in f:
		#print line
		if 'input: DB:' in line or 'input: CUR:' in line or 'status code' in line:
			continue
		line = line.strip()
		line = line.replace('input:', ':param')
		line = line.replace('output:', ':returns:')
		line = line.replace('(optional):', '(optional)')

		if method and method == 'get' and klass == 'Cursor' and 'xt: (optional)' in line:
			line = ':returns: tuple (key, value) of the current record'

		if method and method == 'get' and klass == 'DB' and 'xt: (optional)' in line:
			line = ':returns: the value of the record'

		if method and method in 'get_bulk' and klass == 'DB' and ':param (optional)' in line:
			line = ':param keys: list of keys of the records to retrieve'

		if method and method in 'remove_bulk' and klass == 'DB' and ':param (optional)' in line:
			line = ':param keys: list of keys of the records to remove'

		if method and method in 'set_bulk' and klass == 'DB' and ':param (optional)' in line:
			line = ':param recs: dictionary (key=>value) of records to set'

		if method and method in 'play_script' and klass == 'DB' and ':param (optional)' in line:
			line = ':param args: arguments to the script'

		if method and method == 'get_bulk' and '(optional) arbitrary keys which' in line:
			line = ':returns: dictionary (key=>value) of records'


		if '/rpc/' in line:
			if method:
				doc = [doc[0], ''] + doc[1:]
				docstring = '\n'.join(doc)
				docstring = docstring.replace('"', '\\"')
				s = '%%feature("docstring", "%(docstring)s") kyototycoon::%(klass)s::%(method)s;' % locals()
				if method not in ('void'):
					of.write(s + '\n\n\n\n')
				doc = []

			method = line.split('/')[2]
			if 'cur_' in method:
				klass = 'Cursor'
				method = method[4:]
			else:
				klass = 'DB'
		else:
			doc.append(line)

'''
import sys
sys.path.append('..')

import kyototycoon
print kyototycoon.DB.set_bulk.__doc__
'''