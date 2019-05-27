# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from _sadm import log, env

_cfgfile = path.join(path.sep, 'etc', 'opt', 'sadm', 'deploy.cfg')

def cmdArgs(parser):
	p = parser.add_parser('deploy', help = 'deploy sadm.env')
	p.set_defaults(command = 'deploy')

def main(args):
	log.debug("deploy %s/%s" % (args.profile, args.env))
	rc, _ = env.run(args.profile, args.env, 'deploy', cfgfile = _cfgfile)
	return rc
