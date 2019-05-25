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
	env = path.basename(envfn)[:-4]
	rootdir = path.dirname(path.dirname(envfn))
	deploydir = path.join(rootdir, 'deploy')
	envcmd = path.join(rootdir, 'bin', 'sadm.env')
	for ext in ('.env', '.env.asc', '.zip'):
		fn = env + ext
		if not path.isfile(fn) and ext == '.env.asc':
			continue
		dstfn = path.join(deploydir, fn)
		print('IMPORT:', fn, '->', dstfn)
	return 0
