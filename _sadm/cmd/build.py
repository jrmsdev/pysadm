# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
from _sadm import log, build
from _sadm.errors import Error, EnvError
from _sadm.env import Env
from _sadm.cmd import flags

def _getArgs():
	parser = flags.new('sadm-build', desc = 'build sadm env')
	return flags.parse(parser)

def main():
	args = _getArgs()
	log.debug("build %s/%s" % (args.profile, args.env))
	try:
		env = Env(args.profile, args.env)
		build.run(env)
	except EnvError:
		return 1
	except Error as err:
		log.error("%s" % err)
		return 2
	return 0

if __name__ == '__main__':
	sys.exit(main())
