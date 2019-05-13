# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log
from _sadm.cmd import flags

def main():
	parser = flags.new('sadm-build', desc = 'build sadm profile data')
	parser.add_argument('--name', help = 'profile name', default = '')
	parser.add_argument('cfgfile', help = 'path to config.json file')
	args = flags.parse(parser)
	log.debug(f"cfgfile {args.cfgfile}")
	log.msg('done!')

if __name__ == '__main__':
	main()
