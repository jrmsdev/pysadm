# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

class CheckBuilddir(object):
	_rootdir = None

	def __init__(self, env):
		self._rootdir = env.build.rootdir()

	def content(self):
		assert path.isdir(self._rootdir), "%s builddir not found" % self._rootdir
