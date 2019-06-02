#!/usr/bin/env python3

# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys

from os import path,getenv
from subprocess import call

loglevel = getenv('SADM_LOG', 'warn')

from _sadm import log, env

if __name__ == '__main__':
	log.init(loglevel)
	pname = sys.argv[1]
	rc, _ = env.run('devel', pname, 'build', cfgfile = './docker/sadm.cfg')
	if rc != 0:
		sys.exit(rc)
	# ~ sys.exit(call("./docker/run.sh /opt/sadm/bin/sadm %s %s" % (pname, cfgfn),
		# ~ shell = True))
