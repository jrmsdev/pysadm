# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log

class _webLogger(object):
	_log = None

	def __init__(self):
		self._log = log._logger
		self._log._depth = 4

	def debug(self, msg):
		self._log.debug(msg)

	def error(self, msg):
		self._log.error(msg)

	def warn(self, msg):
		self._log.warn(msg)

	def info(self, msg):
		self._log.info(msg)

	def msg(self, msg):
		self._log.msg(msg)

def init():
	log.info('init web syslog')
	log.setLogger(_webLogger())
