#!/usr/bin/env python3

# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys

from _sadm import listen, libdir
from _sadm.cmd import flags
from _sadm.utils.cmd import callCheck

def main():
	return listen.start()

def uwsgi():
	cmd = [
		'uwsgi',
		'--master',
		'--thunder-lock',
		'--processes', '4',
		'--threads', '2',
		'--need-plugin', 'python3',
		'--http-socket', '127.0.0.1:3666',
		'--virtualenv', sys.exec_prefix,
		'--wsgi-file', libdir.fpath('listen', 'wsgi.py'),
	]
	callCheck(cmd)
	return 0

if __name__ == '__main__':
	if '--uwsgi' in sys.argv:
		sys.exit(uwsgi())
	else:
		sys.exit(main())
