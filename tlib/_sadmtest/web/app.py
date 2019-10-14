# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager

from _sadm import cfg

from _sadmtest import mock
from _sadmtest.wapp import TestingWebapp

__all__ = ['WebApp']

class WebApp(TestingWebapp):
	name = 'web'

	@contextmanager
	def mock(self, tag = 'webapp'):
		mockcfg = cfg.new(self.cfgfn)
		with mock.log(), mock.utils(mockcfg, tag = tag) as ctx:
			try:
				yield ctx
			finally:
				pass
