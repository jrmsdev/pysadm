# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import argparse

from _sadm import log, version

def new(prog, desc = ''):
	p = argparse.ArgumentParser(prog = prog, description = desc)
	p.add_argument('-V', '--version', help = 'show version and exit',
		action = 'version', version = version.string())
	p.add_argument('--debug', help = 'enable debug settings',
		action = 'store_true')
	p.add_argument('--log', help = 'set log level (error)',
		default = 'error', choices = log.levels())
	p.add_argument('--env', help = 'env name (default)',
		metavar = 'name', default = 'default')
	p.add_argument('--profile', help = 'profile name (default)',
		metavar = 'name', default = 'default')
	return p

def parse(p):
	args = p.parse_args()
	if hasattr(args, 'debug') and args.debug:
		log.init('debug')
	else:
		log.init(args.log)
	return args
