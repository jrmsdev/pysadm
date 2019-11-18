# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from _sadm.errors import BuildError
from _sadm.transfer import utils

__all__ = ['cargo']

def cargo(env):
	env.debug('cargo')
	base = path.normpath(env.build.rootdir())
	x = {}
	for ext in ('.zip', '.env', '.env.asc'):
		name = base + ext
		if path.isfile(name):
			env.log("load %s" % path.basename(name))
			x[env.name() + ext] = utils.load(env, name)
		else:
			if ext != '.env.asc':
				raise BuildError("%s file not found" % name)
	return x