# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadmtest import mock

class TestingCmd(object):

	def __init__(self, cfgfile):
		self.cfgfile = cfgfile

	def __enter__(self):
		with mock.utils(self.cfgfile, tag = 'cmd') as utils_ctx:
			self.utils = utils_ctx
			try:
				yield self
			finally:
				pass

	def __exit__(self, *args, **kwargs):
		pass
