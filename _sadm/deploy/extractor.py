# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json

from base64 import b64encode
from os import path, chmod

from _sadm import version
from _sadm.errors import BuildError

_head = """#!/usr/bin/env python3

# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

# sadm.env self extractor
# https://pypi.org/project/sadm/

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
	if path.isfile(env + '.env.asc'):
		rc = system("gpg --verify %s.env.asc %s.env" % (env, env))
		if rc != 0:
			return rc
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
	env.log("%s.deploy" % env.name())
	for ext in ('.zip', '.env', '.env.asc'):
		name = n + ext
		if path.isfile(name):
			env.log("load %s" % path.basename(name))
			cargo[env.name() + ext] = _load(name)
		else:
			if ext != '.env.asc':
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
		fh.write("# sadm version %s\n" % version.get())
		fh.flush()
	chmod(fn, 0o0500)