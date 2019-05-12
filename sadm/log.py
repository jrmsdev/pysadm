# -*- encoding: utf-8 -*-

# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys

def _getCaller():
	inf = sys._getframe(3)
	print('INF:', type(inf), sorted(dir(inf)))
	# ~ print('f_back:', inf.f_back)
	# ~ print('f_builtins:', inf.f_builtins)
	print('f_code:', type(inf.f_code), sorted(dir(inf.f_code)))
	return inf

def debug(msg, *args):
	print('D:', _getCaller(), msg, *args, file = sys.stderr)

def error(msg, *args):
	print('E:', msg, *args, file = sys.stderr)

def info(msg, *args):
	print('I:', msg, *args, file = sys.stderr)

def msg(msg, *args):
	print(msg, *args, file = sys.stdout)
