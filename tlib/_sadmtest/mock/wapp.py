# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

class TestingWebapp(object):
	name = None
	response = None

	def POST(self, datname, callback, *args):
		self.response = callback(*args)
