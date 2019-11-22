# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from _sadm.errors import CommandError
from _sadm.host import host

__all__ = ['main', 'flags']

def flags(p):
	p.add_argument('--exec', help = 'exec filename in env host, remotely',
		metavar = 'filename', default = '')

def main(env, args):
	env.debug("main %s" % env.name())
	if args.exec != '':
		fn = path.abspath(args.exec)
		host.exec(env, fn)
	else:
		raise CommandError('no action', rc = 19)
	return 0
