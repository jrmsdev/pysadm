# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys

# colors

_colored = sys.stdout.isatty() and sys.stderr.isatty()

cyan = lambda text: text
red = lambda text: text
yellow = lambda text: text
blue = lambda text: text
green = lambda text: text

if _colored:
	cyan = lambda text: '\033[0;36m' + text + '\033[0m'
	red = lambda text: '\033[0;31m' + text + '\033[0m'
	yellow = lambda text: '\033[0;33m' + text + '\033[0m'
	blue = lambda text: '\033[0;34m' + text + '\033[0m'
	green = lambda text: '\033[0;32m' + text + '\033[0m'

# debug file prefix

def _getPrefixIdx():
	idx = __file__.find('pysadm')
	if idx <= 0:
		return 0
	return idx + 7

_idx = _getPrefixIdx()

def _getCaller(depth = 2):
	inf = sys._getframe(depth)
	return "%s:%d" % (inf.f_code.co_filename[_idx:], inf.f_lineno)

# setup logger

class sysLogger(object):

	def __init__(self, level):
		self.debug = self._off
		self.warn = self._off
		self.error = self._off
		self.info = self._off
		self.msg = self._off
		self._initLevel(level)

	def _initLevel(self, level):
		if level == 'error':
			self.debug = self._off
			self.warn = self._off
			self.error = self._error
			self.info = self._info
			self.msg = self._msg
		elif level == 'warn':
			self.debug = self._off
			self.warn = self._warn
			self.error = self._error
			self.info = self._info
			self.msg = self._msg
		elif level == 'debug':
			self.debug = self._debug
			self.warn = self._warn
			self.error = self._error
			self.info = self._info
			self.msg = self._msg
		elif level == 'quiet':
			self.debug = self._off
			self.warn = self._off
			self.error = self._error
			self.info = self._off
			self.msg = self._off
		elif level == 'off':
			self.debug = self._off
			self.warn = self._off
			self.error = self._off
			self.info = self._off
			self.msg = self._off
		else:
			raise RuntimeError(f"invalid log level: {level}")

	def _off(self, msg):
		pass

	def _debug(self, msg):
		print(cyan(_getCaller()), cyan(msg), file = sys.stderr)

	def _error(self, msg):
		print(red(msg), file = sys.stderr)

	def _warn(self, msg):
		print(yellow(msg), file = sys.stderr)

	def _info(self, msg):
		print(blue(msg), file = sys.stdout)

	def _msg(self, msg):
		print(green(msg), file = sys.stdout)

class dummyLogger(object):
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

_logger = dummyLogger()

# public methods

def init(level):
	global _logger
	_logger = sysLogger(level)

def levels():
	return ['debug', 'error', 'warn', 'quiet', 'off']

def debug(msg):
	_logger.debug(msg)

def error(msg):
	_logger.error(msg)

def warn(msg):
	_logger.warn(msg)

def info(msg):
	_logger.info(msg)

def msg(msg):
	_logger.msg(msg)
