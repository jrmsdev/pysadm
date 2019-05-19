# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from configparser import ConfigParser

from _sadm.configure import pluginsList, getPlugin
from _sadm.errors import EnvError

__all__ = ['Settings2']

class Settings2(ConfigParser):
	_profile = None
	_env = None

	def __init__(self, profile, env):
		super().__init__(defaults = {}, allow_no_value = False, delimiters = '=',
			comment_prefixes = ('#',), strict = True, default_section = 'default')
		self._profile = profile
		self._env = env

	def plugins(self, action):
		if action == 'configure':
			raise EnvError('invalid settings plugin action: configure')
		for p in pluginsList():
			if self.has_section(p):
				yield (p, getPlugin(p, action))
