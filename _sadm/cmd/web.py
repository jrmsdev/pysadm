# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log, version, web
from _sadm.cmd import flags

def _getArgs():
	p = flags.new('sadm-web', desc = 'sadm web interface')
	p.add_argument('--address', help = 'bind to ip address (localhost)',
		metavar = 'address', default = 'localhost')
	p.add_argument('--port', help = 'bind to tcp port (3478)',
		metavar = 'number', type = int, default = 3478)
	return flags.parse(p)

def main():
	args = _getArgs()
	log.info("sadm-web v%s" % version.get())
	web.start(args.address, args.port)
	log.msg('done!')

if __name__ == '__main__':
	main()
