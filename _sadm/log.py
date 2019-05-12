# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys

# colors

if sys.stdout.isatty() and sys.stderr.isatty():
	cyan = lambda text: '\033[0;36m' + text + '\033[0m'
	red = lambda text: '\033[0;31m' + text + '\033[0m'
	yellow = lambda text: '\033[0;33m' + text + '\033[0m'
else:
	cyan = lambda text: text
	red = lambda text: text
	yellow = lambda text: text

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

# public methods

def debug(msg, *args):
	print(cyan('D:'), _getCaller(), msg, *args, file = sys.stderr)

def error(msg, *args):
	print(red('E:'), msg, *args, file = sys.stderr)

def warn(msg, *args):
	print(yellow('W:'), msg, *args, file = sys.stderr)

def msg(msg, *args):
	print(msg, *args, file = sys.stdout)
