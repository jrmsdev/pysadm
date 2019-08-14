# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path
from unittest.mock import Mock

class MockTmpFile(object):
	_fn = None

	def __init__(self, suffix = None, prefix = None, dir = None):
		if suffix is None:
			suffix = '.mock'
		if prefix is None:
			prefix = __name__
		if dir is None:
			dir = path.join(path.sep, 'tmp')
		self._fn = path.join(dir, prefix + suffix)

	def __enter__(self):
		return self

	def __exit__(self, *args):
		pass

	def close(self):
		pass

	def unlink(self):
		pass

	def write(self, data):
		pass

	def name(self):
		return self._fn

class MockShUtil(object):
	_mock = None
	_expect = None
	makedirs = None
	chmod = None
	chown = None
	mktmp = None
	getcwd = None
	chdir = None

	def __init__(self, cfg):
		self._mock = Mock()
		self.makedirs = self._mock.mock_makedirs
		self.chmod = self._mock.mock_chmod
		self.chown = self._mock.mock_chown
		self.mktmp = self._mock.mock_mktmp
		self.getcwd = self._mock.mock_getcwd
		self.chdir = self._mock.mock_chdir
		self._expect = []
		self._configure(cfg)

	def _configure(self, cfg):
		self.mktmp.side_effect = self._mktmp
		if cfg is None:
			return
		self._utilsExpect(cfg)

	def _utilsExpect(self, cfg):
		data = cfg.get('shutil', fallback = '')
		if data != '':
			for l in data.splitlines():
				l = l.strip()
				if l != '':
					self._expect.append(l)

	def _mktmp(self, suffix = None, prefix = None, dir = None):
		return MockTmpFile(suffix = suffix, prefix = prefix, dir = dir)

	def check(self): # TODO!!
		got = []
		for x in self._mock.mock_calls:
			xname = x[0].replace('mock_', '', 1)
			xargs = x[1]
			xkwargs = x[2]
			cmdline = "%s %s" % (xname, ' '.join([str(i) for i in xargs]))
			for k, v in xkwargs.items():
				v = str(v)
				cmdline = "%s, %s=%s" % (cmdline, k, v)
			got.append(cmdline)
		assert got == self._expect, \
			"shutil got: %s - expect: %s" % (got, self._expect)
