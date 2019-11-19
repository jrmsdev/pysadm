# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json

from base64 import b64encode
from os import path, unlink

from _sadm import version, libdir
from _sadm.errors import BuildError

__all__ = ['gen']

def gen(env):
	_vars = {
		'env': env.name(),
		'rootdir': env.profile.config.get('sadm', 'install.prefix'),
	}
	try:
		env.log("%s.deploy.artifact" % env.name())
		base = path.normpath(env.build.rootdir())
		fn = base + '.deploy.artifact'
		if path.isfile(fn):
			unlink(fn)
		_write(fn, _vars)
	except FileExistsError:
		raise BuildError("%s file exists" % fn)
	return fn

def _write(fn, _vars):
	sk = True
	indent = '\t'
	with libdir.fopen('deploy', 'self_extract.py') as src:
		with open(fn, 'x', encoding = 'utf-8') as fh:
			for line in src.readlines():
				if line.startswith('_vars'):
					fh.write("_vars = %s\n" % json.dumps(_vars,
						indent = indent, sort_keys = sk))
				else:
					fh.write(line)
			fh.write("\n# %s\n" % version.string('sadm'))
			fh.flush()
