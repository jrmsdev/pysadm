# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

def run(env, action):
	env.start('run')
	env.configure()
	env.end('run')
	env.report()
