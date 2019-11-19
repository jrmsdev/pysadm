# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from os import path, makedirs
from shutil import rmtree
from unittest.mock import Mock

from _sadm import cfg

from _sadmtest import mock

class TransferCtx(object):

	def __init__(self, env, artifact):
		self.env = env
		self.artifact = artifact
		self.artifactfn = path.join('tdata', 'build',
			'transfer', "%s.%s.artifact" % (env.name(), artifact))
		self.extractorfn = path.join('tdata', 'build',
			'transfer', "%s.%s" % (env.name(), artifact))
		self.envfn = path.join('tdata', 'build',
			'transfer', "%s.env" % env.name())
		self.zipenvfn = path.join('tdata', 'build',
			'transfer', "%s.zip" % env.name())
		self.tmpdir = path.join('tdata', 'tmp',
			'transfer', env.name())
		self.rootdir = path.join(self.tmpdir, 'rootdir')

	@contextmanager
	def mock(self):
		mockcfg = cfg.new(path.join('tdata', 'transfer', self.env.name(), 'config.ini'))
		with mock.log(), mock.utils(mockcfg, tag = 'transfer'):
			try:
				print('mock.transfer')
				if path.isdir(self.rootdir):
					print('mock.transfer rmtree', self.rootdir)
					rmtree(self.rootdir)
				makedirs(self.tmpdir)
				yield self
			finally:
				print('mock.transfer.restore')
				rmtree(self.tmpdir)
