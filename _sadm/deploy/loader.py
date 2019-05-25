# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
from os import path, system, makedirs, unlink
from shutil import move

def loadenv(filename):
	envfn = path.realpath(filename)
	print("%s: load" % envfn)
	if path.isfile(envfn + '.asc'):
		rc = system("gpg --no-tty --no --verify %s.asc %s 2>/dev/null" % (envfn, envfn))
		if rc != 0:
			print("env signature verify failed!", file = sys.stderr)
			return 1
	rc = system("sha256sum -c %s" % envfn)
	if rc != 0:
		print("env checksum failed!", file = sys.stderr)
		return 2
	return _importenv(envfn)

def _importenv(envfn):
	basefn = envfn[:-4]
	rootdir = path.dirname(path.dirname(envfn))
	deploydir = path.join(rootdir, 'deploy')
	makedirs(deploydir, exist_ok = True)
	# ~ envcmd = path.join(rootdir, 'bin', 'sadm.env')
	for ext in ('.env', '.zip'):
		fn = basefn + ext
		dstfn = path.join(deploydir, path.basename(fn))
		if path.isfile(dstfn):
			unlink(dstfn)
		print("%s:" % fn, dstfn)
		move(fn, dstfn)
	return 0
