# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.configure import pluginsList

__all__ = ['Settings']

class Settings(object):
	_data = None
	_plugins = None

	def __init__(self, data):
		self._data = data
		self._plugins = {}
		for p in self._data.keys():
			self._plugins[p] = True

	def plugins(self):
		for p in pluginsList():
			if self._plugins.get(p, False):
				yield p
