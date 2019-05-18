# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

def run(env):
	env.debug('run')
	env.start('build')
	for p in env.settings.plugins('build'):
		p.build(env)
	env.end('build')
