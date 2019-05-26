# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log

def cmdArgs(parser):
	p = parser.add_parser('import', help = 'import sadm.env')
	p.add_argument('filename', help = 'sadm.env file to import')

def main():
	args = _getArgs()
	log.debug("import %s/%s" % (args.profile, args.env))
	# ~ rc, _ = env.run(args.profile, args.env, 'deploy')
	# ~ return rc
	return 128
