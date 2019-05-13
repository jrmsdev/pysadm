# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import argparse

from _sadm import log

def new(prog, desc = ''):
	p = argparse.ArgumentParser(prog = prog, description = desc)
	p.add_argument('--log', help = 'set log level', default = 'error',
		choices = log.levels())
	return p

def parse(p):
	args = p.parse_args()
	print('LOG:', args.log)
	log.init(args.log)
	return args
