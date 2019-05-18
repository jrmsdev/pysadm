# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import getcwd
from time import strftime

def run(env, action):
	env.start('run', "%s %s" % (action, strftime('%c %z')))
	env.log(getcwd())
	env.configure()
	env.end('run')
	env.report()
