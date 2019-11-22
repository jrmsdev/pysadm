#!/usr/bin/env python3

# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
from _sadm import log
from _sadm.cmd import flags
from _sadm.env import Env
from _sadm.errors import Error, CommandError
from _sadm.setup import setup

def _getArgs(argv):
	parser = flags.new('sadm-setup', desc = 'sadm setup')
	return flags.parse(parser, argv)

def main(argv = None):
	if argv is None:
		argv = sys.argv[1:] # pragma: no cover
	args = _getArgs(argv)
	log.debug("profile %s/%s" % (args.profile, args.env))
	rc = 128
	try:
		env = Env(args.profile, args.env)
		env.configure()
		rc = setup.run(env)
	except CommandError as err:
		log.error("%s" % err)
		return err.rc
	except Error as err:
		log.error("%s" % err)
		return 9
	return rc

if __name__ == '__main__':
	sys.exit(main()) # pragma: no cover
