# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
from _sadm import log, env
from _sadm.cmd import flags
from _sadm.cmd.deploy import loader

def _getArgs():
	parser = flags.new('sadm', desc = 'deploy sadm env')
	subparser = parser.add_subparsers(title = 'commands',
		description = 'run `sadm command -h` for more information',
		help = 'description')
	loader.cmdArgs(subparser)
	return flags.parse(parser)

def main():
	args = _getArgs()
	log.debug("deploy %s/%s" % (args.profile, args.env))
	# ~ rc, _ = env.run(args.profile, args.env, 'deploy')
	# ~ return rc
	return 128

if __name__ == '__main__':
	sys.exit(main())
