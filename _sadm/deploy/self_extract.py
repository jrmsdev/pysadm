#!/usr/bin/env python3

# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

# sadm.env deploy artifact
# https://pypi.org/project/sadm/

import sys

from os import path
from subprocess import call

_vars = {}

def main():
	env = _vars['env']
	rootdir = _vars['rootdir']
	dstdir = path.join(rootdir, 'env')
	envfn = path.join(dstdir, "%s.env" % env)
	envcmd = path.join(rootdir, 'bin', 'sadm')
	rc = call("%s import %s" % (envcmd, envfn), shell = True)
	if rc != 0:
		return rc
	rc = call("%s --env %s deploy" % (envcmd, env), shell = True)
	if rc != 0:
		return rc
	return 0

if __name__ == '__main__':
	sys.exit(main()) # pragma: no cover
