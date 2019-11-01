# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from contextlib import contextmanager
from os import path
from unittest.mock import Mock

from _sadm import cfg

import _sadm.devops.wapp.tpl.tpl
import _sadm.devops.wapp.wapp

from _sadmtest import mock
from _sadmtest.wapp import TestingWebapp

class DevopsWebapp(TestingWebapp):
	name = 'devops'

	@contextmanager
	def mock(self, tag = 'devops'):
		mockcfg = None
		if path.isfile(self.cfgfn):
			mockcfg = cfg.new(self.cfgfn)
		bup = Mock()
		bup.bottle = bup.mock.bottle
		bup.bottle.template = bottle.template
		bup.wapp = _sadm.devops.wapp.wapp.wapp
		bup.tpl = bup.mock.tpl
		bup.tpl.parse = _sadm.devops.wapp.tpl.tpl.parse
		with mock.log(), mock.utils(mockcfg, tag = tag):
			ctx = Mock()
			ctx.orig = bup
			# mock bottle
			ctx.bottle = ctx.mock.bottle
			ctx.bottle.template = ctx.mock.bottle.template
			bottle.template = ctx.bottle.template
			# mock wapp
			_sadm.devops.wapp.wapp.init(cfgfn = self.cfgfn)
			ctx.wapp = ctx.mock.wapp
			_sadm.devops.wapp.wapp.wapp = ctx.wapp
			ctx.config = _sadm.devops.wapp.wapp.config
			# mock tpl
			ctx.tpl = ctx.mock.tpl
			ctx.tpl.parse = ctx.mock.tpl.parse
			_sadm.devops.wapp.tpl.tpl.parse = ctx.tpl.parse
			try:
				yield ctx
			finally:
				bottle.template = None
				bottle.template = bup.bottle.template
				_sadm.devops.wapp.wapp.wapp = None
				_sadm.devops.wapp.wapp.wapp = bup.wapp
				_sadm.devops.wapp.wapp.config = None
				_sadm.devops.wapp.tpl.tpl.parse = None
				_sadm.devops.wapp.tpl.tpl.parse = bup.tpl.parse
