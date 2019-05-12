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

def debug(msg):
	# ~ print(cyan(_getCaller()), cyan(msg), file = sys.stderr)
	_logger.debug(msg)

def error(msg):
	# ~ print(red(msg), file = sys.stderr)
	_logger.error(msg)

def warn(msg):
	# ~ print(yellow(msg), file = sys.stderr)
	_logger.warn(msg)

def info(msg):
	# ~ print(blue(msg), file = sys.stdout)
	_logger.info(msg)

def msg(msg):
	# ~ print(green(msg), file = sys.stdout)
	_logger.msg(msg)
