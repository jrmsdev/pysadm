# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

class MockRequest(object):
	pass

class MockWebapp(object):
	name = None
	response = None

	def POST(self, datname, callback, *args):
		self.response = callback(*args)
