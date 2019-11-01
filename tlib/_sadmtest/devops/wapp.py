# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from unittest.mock import Mock

from _sadm import cfg

from _sadmtest import mock
from _sadmtest.wapp import TestingWebapp

class DevopsWebapp(TestingWebapp):
	name = 'devops'

	@contextmanager
	def mock(self, tag = 'devops'):
		mockcfg = None
		if path.isfile(self.cfgfn):
			mockcfg = cfg.new(self.cfgfn)
		with mock.log(), mock.utils(mockcfg, tag = tag):
			ctx = Mock()
			try:
				yield ctx
			finally:
				pass
