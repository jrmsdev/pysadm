# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from _sadmtest.listen.webhook.repo.provider import TestingProvider
from _sadmtest.mock.wapp import TestingWebapp, MockWebapp

import _sadm.listen.wapp
_sadm.listen.wapp.wapp = MockWebapp()

import _sadm.listen.webhook.repo
_sadm.listen.webhook.repo._provider['testing'] = TestingProvider()

class ListenWebapp(TestingWebapp):
	name = 'listen'

	def __init__(self, profile):
		self._profile = profile
		self.wapp = _sadm.listen.wapp

	def __enter__(self):
		_sadm.listen.wapp.init(cfgfn = path.join('tdata', 'listen.cfg'))
		if self._profile != '':
			parts = ['tdata', 'listen']
			parts.extend(self._profile.split('/'))
			parts.append('listen.cfg')
			fn = path.join(*parts)
			with open(fn, 'r') as fh:
				_sadm.listen.wapp.config.read_file(fh)
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		del _sadm.listen.wapp.config
		_sadm.listen.wapp.config = _sadm.listen.wapp._newConfig()
