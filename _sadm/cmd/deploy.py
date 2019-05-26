# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
from _sadm import log, env
from _sadm.cmd import flags

def _getArgs():
	parser = flags.new('sadm', desc = 'deploy sadm env')
	return flags.parse(parser)

def main():
	args = _getArgs()
	log.debug("deploy %s/%s" % (args.profile, args.env))
	# ~ rc, _ = env.run(args.profile, args.env, 'deploy')
	# ~ return rc
	return 128

if __name__ == '__main__':
	sys.exit(main())
