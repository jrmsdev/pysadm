# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

def run(env):
	env.debug('run')
	env.start('build')
	for p, mod in env.settings.plugins('build'):
		tag = "build.%s" % p
		env.start(tag)
		mod.build(env)
		env.end(tag)
	env.end('build')
