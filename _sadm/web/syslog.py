# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
from _sadm import log

class _webLogger(object):

	def debug(self, msg, caller = None):
		print("[SYSLOG] D: %s: %s" % (caller, msg), file = sys.stderr)

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
