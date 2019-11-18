# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from os import path
from unittest.mock import Mock

from _sadm import cfg

from _sadmtest import mock

class TransferCtx(object):

	def __init__(self, env):
		self.env = env
		self.extractorfn = path.join('tdata', 'build', 'transfer', 'testing.deploy')
		self.envfn = path.join('tdata', 'build', 'transfer', 'testing.env')
		self.zipenvfn = path.join('tdata', 'build', 'transfer', 'testing.zip')

	@contextmanager
	def mock(self):
		mockcfg = cfg.new(path.join('tdata', 'transfer', self.env.name(), 'config.ini'))
		with mock.log(), mock.utils(mockcfg, tag = 'transfer'):
			try:
				print('mock.transfer')
				yield self
			finally:
				print('mock.transfer.restore')
