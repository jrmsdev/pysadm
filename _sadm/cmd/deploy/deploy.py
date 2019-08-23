# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from _sadm import log
from _sadm.deploy import cmd

def cmdArgs(parser):
	p = parser.add_parser('deploy', help = 'deploy sadm.env')
	p.set_defaults(command = 'deploy')

def main(args, sumode):
	log.debug("deploy %s sumode=%s" % (args.env, sumode))
	return cmd.run(args.env, sumode)
