# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
from os import path, chdir, system

def loadenv(filename):
	envdir = path.realpath(path.dirname(filename))
	envfn = path.basename(filename)
	print(envdir)
	chdir(envdir)
	if path.isfile(envfn + '.asc'):
		rc = system("gpg --no-tty --no --verify %s.asc %s 2>/dev/null" % (envfn, envfn))
		if rc != 0:
			print("env signature verify failed!", file = sys.stderr)
			return rc
	rc = system("sha256sum -c %s" % envfn)
	if rc != 0:
		print("env checksum failed!", file = sys.stderr)
		return rc
	return _importenv(envfn)

def _importenv(envfn):
	rootdir = path.dirname(path.dirname(envfn))
	deploydir = path.join(rootdir, 'deploy')
	return 0
