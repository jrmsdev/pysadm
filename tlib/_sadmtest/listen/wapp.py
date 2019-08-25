# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from _sadmtest import mock
from _sadmtest.listen.webhook.repo.provider import TestingProvider
from _sadmtest.wapp import TestingWebapp

import _sadm.listen.wapp
import _sadm.listen.webhook.repo
_sadm.listen.webhook.repo._provider['testing'] = TestingProvider()

class ListenWebapp(TestingWebapp):
	name = 'listen'

	def __mockConfig(self):
		return None # FIXME

	def __enter__(self):
		fn = path.join('tdata', 'listen.cfg')
		_sadm.listen.wapp.config = _sadm.listen.wapp._newConfig(fn)
		if self.profile != '':
			fn = path.join('tdata', 'listen', self.profile, 'listen.cfg')
			with open(fn, 'r') as fh:
				_sadm.listen.wapp.config.read_file(fh)
		with mock.utils(self.__mockConfig()):
			return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		del _sadm.listen.wapp.config
