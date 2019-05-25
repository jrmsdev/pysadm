#!/usr/bin/env python3

# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

# sadm.env self extractor
# https://pypi.org/project/sadm/

import sys
from base64 import b64decode
from os import path, makedirs, system, chdir, chmod
from shutil import rmtree

_cargo = {}
_vars = {}

def extract():
	env = _vars['.env']
	dstdir = _vars['.destdir']
	if path.isdir(dstdir):
		rmtree(dstdir)
	makedirs(dstdir, exist_ok = True)
	chmod(dstdir, 0o0700)
	for fn, data in _cargo.items():
		fn = path.join(dstdir, fn)
		with open(fn, 'wb') as fh:
			fh.write(b64decode(data.encode()))
	chdir(dstdir)
	if path.isfile(env + '.env.asc'):
		rc = system("gpg --no-tty --no --verify %s.env.asc %s.env 2>/dev/null" % (env, env))
		if rc != 0:
			print("env signature verify failed!", file = sys.stderr)
			return rc
	return system("sha256sum -c %s.env" % env)

if __name__ == '__main__':
	sys.exit(extract())
