#!/usr/bin/env python3

# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
from subprocess import call

if __name__ == '__main__':
	pname = sys.argv[1]
	try:
		cfgfn = sys.argv[2]
	except IndexError:
		cfgfn = 'configure.ini'
	print('CFGFN:', cfgfn)
	sys.exit(call("./docker/run.sh /opt/sadm/bin/sadm-plugin %s %s" % (pname, cfgfn),
		shell = True))
