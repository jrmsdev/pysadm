# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from os import path

from _sadmtest import mock
from _sadmtest.listen.webhook.repo.provider import TestingProvider
from _sadmtest.wapp import TestingWebapp

import _sadm.listen.wapp
import _sadm.listen.webhook.repo
_sadm.listen.webhook.repo._provider['testing'] = TestingProvider()

class ListenWebapp(TestingWebapp):
	name = 'listen'

	def __enter__(self):
		print("listen wapp init %s" % self.profile)
		fn = path.join('tdata', 'listen.cfg')
		if self.profile != '.':
			fn = path.join('tdata', 'listen', self.profile, 'listen.cfg')
		_sadm.listen.wapp.wapp = _sadm.listen.wapp.init(cfgfn = fn)
		with mock.utils(_sadm.listen.wapp.config):
			return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		del _sadm.listen.wapp.config
		del _sadm.listen.wapp.wapp
		_sadm.listen.wapp.wapp = bottle.Bottle()

	@property
	def routes(self):
		return _sadm.listen.wapp.wapp.routes
