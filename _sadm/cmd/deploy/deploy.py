# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log
from _sadm.deploy import cmd
from _sadm.utils import sh, path

def cmdArgs(parser):
	p = parser.add_parser('deploy', help = 'deploy sadm.env')
	p.set_defaults(command = 'deploy')

def main(args, sumode):
	log.debug("deploy %s sumode=%s" % (args.env, sumode))
	if sumode:
		_sumode()
	else:
		dn = path.join('~', '.local', 'sadm', 'deploy')
		sh.makedirs(dn, mode = 0o750, exists_ok = True)
		with sh.lockd(dn):
			with sh.mktmpdir(dir = dn, prefix = '', rmtree = True) as tmpdir:
				print(tmpdir)
	return cmd.run(args.env, sumode)

def _sumode():
	pass
