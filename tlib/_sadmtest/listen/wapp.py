# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

import _sadm.listen.wapp

from _sadmtest.mock.wapp import MockWebapp

class ListenWebapp(MockWebapp):
	name = 'listen'

	def __init__(self, profile):
		self._profile = profile

	def __enter__(self):
		_sadm.listen.wapp._mockWebapp = True
		self.wapp = _sadm.listen.wapp.init(cfgfn = path.join('tdata', 'listen.cfg'))
		if self._profile != '':
			parts = ['tdata', 'listen']
			parts.extend(self._profile.split('/'))
			parts.append('listen.cfg')
			fn = path.join(*parts)
			with open(fn, 'r') as fh:
				_sadm.listen.wapp.config.read_file(fh)
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		_sadm.listen.wapp._mockWebapp = False
		del _sadm.listen.wapp.config
		_sadm.listen.wapp.config = _sadm.listen.wapp._newConfig()
