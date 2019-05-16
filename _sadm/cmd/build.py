# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log
from _sadm.env import Env
from _sadm.cmd import flags

def _getArgs():
	parser = flags.new('sadm-build', desc = 'build sadm env')
	parser.add_argument('cfgfile', help = 'path to config.json file')
	return flags.parse(parser)

def main():
	args = _getArgs()
	log.debug("cfgfile %s" % args.cfgfile)
	try:
		env = Env(args.profile, args.env, args.cfgfile)
	except Exception as err:
		log.error("%s" % err)
	else:
		log.msg('done!')

if __name__ == '__main__':
	main()
