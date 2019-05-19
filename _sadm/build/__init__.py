# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

_builddir = path.realpath('./build')

def run(env):
	env.debug('run')
	for p, mod in env.settings.plugins('build'):
		tag = "build.%s" % p
		env.start(tag)
		mod.build(env)
		env.end(tag)
