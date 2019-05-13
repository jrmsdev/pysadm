# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log
from _sadm.cmd import flags

def main():
	parser = flags.new('sadm-build', desc = 'build sadm profile data')
	args = flags.parse(parser)
	log.debug('main')
	log.warn('warning...')
	log.error('error...')
	log.info('info...')
	log.msg('done!')

if __name__ == '__main__':
	main()
