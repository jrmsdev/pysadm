# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log

class _webLogger(object):
	def close(self):
		pass

	def debug(self, msg):
		pass

	def error(self, msg):
		pass

	def warn(self, msg):
		pass

	def info(self, msg):
		pass

	def msg(self, msg):
		pass

def init():
	log.info('init web syslog')
	log.setLogger(_webLogger())
