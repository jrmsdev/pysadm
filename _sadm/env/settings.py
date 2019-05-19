# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json

from _sadm.configure import pluginsList, getPlugin
from _sadm.errors import EnvError

__all__ = ['Settings']

class Settings(object):
	_data = {}
	_plugins = {}
	_done = {}

	def write(self, fh, indent = False):
		sk = False
		i = None
		if indent:
			# ~ sk = True
			i = '\t'
		json.dump(self._data, fh, allow_nan = False, sort_keys = sk, indent = i)

	def plugins(self, action):
		if action == 'configure':
			raise EnvError('invalid settings plugin action: configure')
		if self._done.get(action, False):
			raise EnvError("env action %s already done" % action)
		self._done[action] = True
		for p in pluginsList():
			if self._plugins.get(p, False):
				yield (p, getPlugin(p, action))

	def init(self, plugin, data):
		self._data[plugin] = data
