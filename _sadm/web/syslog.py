# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
import sqlite3

from _sadm import log

class _webLogger(object):

	def __init__(self):
		self.db = _dbInit()

	def error(self, msg):
		print("[SYSLOG] E:", msg, file = sys.stderr)

	def warn(self, msg):
		print("[SYSLOG] W:", msg, file = sys.stderr)

	def info(self, msg):
		print("[SYSLOG] I:", msg, file = sys.stdout)

	def msg(self, msg):
		print("[SYSLOG]", msg, file = sys.stdout)

def init():
	log.info('init web syslog')
	log._logger._child = _webLogger()

def _dbInit():
	log.debug('syslog db init')
	return None
