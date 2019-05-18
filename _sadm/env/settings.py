# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

class Settings(object):
	_data = None

	def __init__(self, data, cfg):
		self._data = _load(data, cfg)

def _load(d, c):
	d.update(c)
	return d
