#!/usr/bin/env python3

# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys

from _sadm import listen, libdir
from _sadm.cmd import flags
from _sadm.utils import path
from _sadm.utils.cmd import callCheck

def bottle():
	return listen.start()

def uwsgi():
	crtfn = path.join(path.sep, 'etc', 'ssl', 'certs', 'ssl-cert-snakeoil.pem')
	keyfn = path.join(path.sep, 'etc', 'ssl', 'private', 'ssl-cert-snakeoil.key')
	cmd = [
		'uwsgi',
		'--need-plugin', 'python3',
		'--virtualenv', sys.exec_prefix,
		'--https-socket', "127.0.0.1:3666,%s,%s" % (crtfn, keyfn),
		'--touch-reload', path.join(path.sep, 'run', 'sadm.listen.uwsgi.reload'),
		'--ini', libdir.fpath('listen', 'uwsgi.ini'),
	]
	callCheck(cmd)
	return 0

if __name__ == '__main__':
	if '--bottle' in sys.argv:
		sys.exit(bottle())
	else:
		sys.exit(uwsgi())
