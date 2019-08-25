# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

class MockRequest(object):
	pass

class MockWebapp(object):
	wapp = None
	name = None
	response = None

	def __getCallback(self, name, method):
		for r in self.wapp.routes:
			if r.name == name and r.method == method:
				return r.callback
		assert False, \
			"wapp %s no callback found for route %s method %s" % (self.name, name, method)

	def __newRequest(self):
		return MockRequest()

	def POST(self, datname, routeName, *args):
		callback = self.__getCallback(routeName, 'POST')
		self.wapp.request = self.__newRequest()
		self.response = callback(*args)
