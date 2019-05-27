# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from _sadm import log
from _sadm.deploy.deploy import run

def cmdArgs(parser):
	p = parser.add_parser('deploy', help = 'deploy sadm.env')
	p.set_defaults(command = 'deploy')

def main(args):
	log.debug("deploy %s" % args.env)
	return run(args.env)
