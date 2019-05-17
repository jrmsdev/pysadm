# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

class Settings(object):
	_profile = None
	_env = None
	_filename = None

	def __init__(self, profile, env, cfgfile):
		self._profile = profile
		self._env = env
		self._filename = cfgfile
