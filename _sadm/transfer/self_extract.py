#!/usr/bin/env python3

# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

# sadm.artifact self extractor
# https://pypi.org/project/sadm/

import sys

from base64 import b64decode
from os import path, makedirs, chmod, unlink
from subprocess import call

_cargo = {}
_vars = {}
_artifact = tuple()

def main():
	env = _vars['env']
	rootdir = _vars['rootdir']
	dstdir = path.join(rootdir, 'env')
	artifact = extract(dstdir)
	return call(artifact, shell = True)

def extract(dstdir):
	makedirs(dstdir, exist_ok = True)
	chmod(dstdir, 0o700)
	# cargo
	for fn, data in _cargo.items():
		fn = path.join(dstdir, fn)
		if path.isfile(fn):
			unlink(fn)
		with open(fn, 'wb') as fh:
			fh.write(b64decode(data.encode()))
	# artifact
	artn = _artifact[0]
	artfn = path.join(dstdir, artn)
	if path.isfile(artfn):
		unlink(artfn)
	with open(artfn, 'wb') as fh:
		fh.write(b64decode(_artifact[1].encode()))
	chmod(artfn, 0o700)
	return artfn

if __name__ == '__main__':
	sys.exit(main()) # pragma: no cover
