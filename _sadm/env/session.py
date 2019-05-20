# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from time import time

from _sadm.errors import SessionError

__all__ = ['Session']

class Session(object):
	_start = None
	_d = None

	def __init__(self):
		self._d = {}

	def start(self):
		if _start is not None:
			raise SessionError('session already started')
		self._start = time()

	def stop(self):
		if _start is None:
			raise SessionError('session not started')
		took = time() - self._start
		del self._start
		return took

	def set(self, opt, val):
		if self._d.get(opt, None) is not None:
			raise SessionError("%s option already set" % opt)
		self._d[opt] = val

	def get(self, opt, default = None):
		if self._d.get(opt, None) is None:
			if default is None:
				raise SessionError("%s option not set" % opt)
			else:
				return default
		return self._d[opt]
