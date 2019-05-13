# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import argparse

from _sadm import log, version

def new(prog, desc = ''):
	p = argparse.ArgumentParser(prog = prog, description = desc)
	p.add_argument('-V', '--version', help = 'show version and exit',
		action = 'version', version = version.string())
	p.add_argument('--log', help = 'set log level',
		default = 'error', choices = log.levels())
	return p

def parse(p):
	args = p.parse_args()
	log.init(args.log)
	return args
