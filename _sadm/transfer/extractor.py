# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json

from os import path

from _sadm import version, libdir
from _sadm.errors import BuildError
from _sadm.transfer import transfer
from _sadm.utils import tmpfile

__all__ = ['gen']

def gen(env, artifact):
	_vars = {
		'env': env.name(),
		'profile': env.profile.name(),
		'rootdir': env.profile.config.get('sadm', 'install.prefix'),
	}
	env.log("gen %s.%s" % (env.name(), artifact))
	cargo = transfer.cargo(env, artifact)
	base = path.normpath(env.build.rootdir())
	return _write(env, artifact, cargo, _vars)

def _write(env, artifact, cargo, _vars):
	env.debug("write %s.%s" % (env.name(), artifact))
	sk = True
	indent = '\t'
	fn = None
	with libdir.fopen('transfer', 'self_extract.py') as src:
		with tmpfile.new(prefix = __name__) as fh:
			fn = fh.name()
			err = None
			try:
				for line in src.readlines():
					if line.startswith('_cargo'):
						fh.write("_cargo = %s\n" % json.dumps(cargo,
							indent = indent, sort_keys = sk))
					elif line.startswith('_vars'):
						fh.write("_vars = %s\n" % json.dumps(_vars,
							indent = indent, sort_keys = sk))
					elif line.startswith('_artifact'):
						fh.write("_artifact = ('%s.%s', '%s')\n" % \
							(env.name(), artifact, transfer.artifact(env, artifact)))
					else:
						fh.write(line)
				fh.write("\n# %s\n" % version.string('sadm'))
				fh.flush()
			except Exception as exc:
				env.debug(str(exc))
				err = exc
			if err is not None:
				fh.close()
				fh.unlink()
				raise BuildError(str(err))
	return fn
