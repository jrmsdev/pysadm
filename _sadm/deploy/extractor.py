# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json

from base64 import b64encode
from os import path, chmod

from _sadm.errors import BuildError

_head = """#!/usr/bin/env python3
# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.
# WWW: https://pypi.org/project/sadm/

from base64 import b64decode
from os import path, makedirs, system, chdir

"""
_tail = """
def extract():
	env = _vars['.env']
	dstdir = _vars['.destdir']
	makedirs(dstdir, exist_ok = True)
	for fn, data in _cargo.items():
		fn = path.join(dstdir, fn)
		with open(fn, 'wb') as fh:
			fh.write(b64decode(data.encode()))
	chdir(dstdir)
	return system("sha256sum -c %s.env" % env)

if __name__ == '__main__':
	import sys
	sys.exit(extract())
"""

def gen(env):
	_vars = {
		'.env': env.name(),
		'.destdir': path.join(path.sep, 'opt', 'sadm', 'env'),
	}
	cargo = {}
	n = path.normpath(env.build.rootdir())
	fn = n + '.deploy'
	env.log("create %s" % fn)
	for ext in ('.zip', '.env'):
		name = n + ext
		if path.isfile(name):
			env.log("add %s" % name)
			cargo[env.name() + ext] = _load(name)
		else:
			raise BuildError("%s file not found" % name)
	_write(fn, cargo, _vars)

def _load(fn):
	with open(fn, 'rb') as fh:
		return b64encode(fh.read()).decode()

def _write(fn, cargo, _vars):
	indent = '\t'
	with open(fn, 'x') as fh:
		fh.write(_head)
		fh.write("_cargo = %s\n" % json.dumps(cargo, indent = indent, sort_keys = True))
		fh.write("_vars = %s\n" % json.dumps(_vars, indent = indent, sort_keys = True))
		fh.write(_tail)
		fh.flush()
	chmod(fn, 0o0500)
