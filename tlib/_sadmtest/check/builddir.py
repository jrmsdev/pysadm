# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

class CheckBuilddir(object):
	_rootdir = None
	_deployfn = None
	_envfn = None
	_metadir = None
	_zipfn = None

	def __init__(self, env):
		self._rootdir = env.build.rootdir()
		self._deployfn = self._rootdir + '.deploy'
		self._envfn = self._rootdir + '.env'
		self._metadir = self._rootdir + '.meta'
		self._zipfn = self._rootdir + '.zip'

	def content(self):
		assert path.isdir(self._rootdir), "%s builddir not found" % self._rootdir
		assert path.isfile(self._deployfn), \
			"%s deploy self-extract file not found" % self._deployfn
		assert path.isfile(self._envfn), \
			"%s deploy .env file not found" % self._envfn
		assert path.isdir(self._metadir), \
			"%s build meta dir not found" % self._metadir
		assert path.isfile(self._zipfn), \
			"%s deploy zip file not found" % self._zipfn