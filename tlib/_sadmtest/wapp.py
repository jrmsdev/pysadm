# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

class TestingWebapp(object):
	name = None
	response = None

	def POST(self, datname, callback, *args):
		self.response = callback(*args)
