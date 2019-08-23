# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
from _sadm import log, env
from _sadm.cmd import flags
from _sadm.cmd.deploy import loader
from _sadm.cmd.deploy import deploy
from _sadm.utils import sh

_parser = flags.new('sadm', desc = 'deploy sadm env')

def _getArgs():
	subparser = _parser.add_subparsers(title = 'commands',
		description = 'run `sadm command -h` for more information',
		help = 'description')
	loader.cmdArgs(subparser)
	deploy.cmdArgs(subparser)
	return flags.parse(_parser)

def main():
	sumode = False
	if '--sumode' in sys.argv:
		sys.argv.remove('--sumode')
		sumode = True

	args = _getArgs()
	log.debug("deploy %s/%s sumode=%s" % (args.profile, args.env, sumode))

	if not sumode and sh.getuid() == 0:
		log.error('do not run as root')
		return 9

	try:
		cmd = args.command
	except AttributeError:
		log.error('invalid usage')
		_parser.print_usage()
		return 1
	log.debug("dispatch command %s" % cmd)

	if args.command == 'import':
		return loader.main(args)

	return deploy.main(args, sumode)

if __name__ == '__main__':
	sys.exit(main())
