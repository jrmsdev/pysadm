# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
from _sadm import log, env
from _sadm.cmd import flags
from _sadm.cmd.deploy import loader
from _sadm.cmd.deploy import deploy as deploy_cmd

_parser = flags.new('sadm', desc = 'deploy sadm env')

def _getArgs():
	subparser = _parser.add_subparsers(title = 'commands',
		description = 'run `sadm command -h` for more information',
		help = 'description')
	loader.cmdArgs(subparser)
	deploy_cmd.cmdArgs(subparser)
	return flags.parse(_parser)

def main():
	args = _getArgs()
	log.debug("deploy %s/%s" % (args.profile, args.env))
	try:
		cmd = args.command
	except AttributeError:
		log.error('invalid usage')
		_parser.print_usage()
		return 1
	print('CMD:', args.command)
	# ~ rc, _ = env.run(args.profile, args.env, 'deploy')
	# ~ return rc
	return 128

if __name__ == '__main__':
	sys.exit(main())
