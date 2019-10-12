# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager

from _sadm import cfg

from _sadmtest import mock

class TestingCmd(object):

	def __init__(self, cfgfile):
		self.cfgfile = cfgfile

	@contextmanager
	def mock(self):
		mockcfg = cfg.new(self.cfgfile)
		with mock.utils(mockcfg, tag = 'cmd') as ctx:
			try:
				yield ctx
			finally:
				pass
