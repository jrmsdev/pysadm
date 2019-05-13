# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log

def main():
	log.init('debug')
	log.debug('main')
	log.warn('warning...')
	log.error('error...')
	log.info('info...')
	log.msg('done!')

if __name__ == '__main__':
	main()
