# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from contextlib import contextmanager
from unittest.mock import Mock

from _sadm import cfg

from _sadmtest import mock
from _sadmtest.wapp import TestingWebapp

__all__ = ['WebApp']

def _mock_decorator(*args, **kwargs):
	def wrapper(func):
		def decorator(*args, **kwargs):
			return func(*args, **kwargs)
		return decorator
	return wrapper

_mock = Mock()
bottle.view = _mock.view
_mock.view.side_effect = _mock_decorator

import _sadm.web.app
import _sadm.web.tpl

_sadm.web.app.wapp = _mock.wapp
_sadm.web.tpl.data = _mock.tpl_data
_mock.web.tpl_data.side_effect = _mock_decorator

class WebApp(TestingWebapp):
	name = 'web'

	@contextmanager
	def mock(self, tag = 'webapp'):
		mockcfg = cfg.new(self.cfgfn)
		with mock.log(), mock.utils(mockcfg, tag = tag):
			try:
				yield _mock
			finally:
				pass
