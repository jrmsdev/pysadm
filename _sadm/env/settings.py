# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

class Settings(object):
	_profile = None
	_env = None

	def __init__(self, profile, env):
		self._profile = profile
		self._env = env
