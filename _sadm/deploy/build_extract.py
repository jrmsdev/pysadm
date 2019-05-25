#!/usr/bin/env python3

# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

# sadm.env self extractor
# https://pypi.org/project/sadm/

import sys

from base64 import b64decode
from os import path, makedirs, chmod
from shutil import rmtree

from _sadm.deploy.loader import loadenv

_cargo = {}
_vars = {}

def extract():
	env = _vars['env']
	rootdir = _vars['rootdir']
	dstdir = path.join(rootdir, 'env')
	if path.isdir(dstdir):
		rmtree(dstdir)
	makedirs(dstdir, exist_ok = True)
	chmod(dstdir, 0o0700)
	for fn, data in _cargo.items():
		fn = path.join(dstdir, fn)
		with open(fn, 'wb') as fh:
			fh.write(b64decode(data.encode()))
	envfn = path.join(dstdir, "%s.env" % env)
	return loadenv(envfn)

if __name__ == '__main__':
	sys.exit(extract())
