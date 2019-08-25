# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from io import BytesIO
from os import path

class TestingWebapp(object):
	profile = ''
	name = None
	response = None

	def __init__(self, profile):
		if profile != '':
			self.profile = path.join(*profile.split('/'))

	def POST(self, pdata, callback, *args):
		bottle.request.environ['wsgi.input'] = BytesIO()
		self.response = callback(*args)
