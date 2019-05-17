# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

def run(env):
	env.setLogtag('build')
	env.debug('run')
	env.log('start')
	env.log('done')
	env.setLogtag('')
