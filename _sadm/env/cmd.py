# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import getcwd
from time import strftime, time

from _sadm import build
from _sadm.errors import EnvError

def run(env, action):
	_start = time()
	env.info("%s start %s" % (action, strftime('%c %z')))
	env.log("%s from %s" % (action, getcwd()))
	try:
		with env.lock() as env:
			env.configure()
			_run(env, action)
			env.report(action, startTime = _start)
	finally:
		env.info("%s end %s" % (action, strftime('%c %z')))

def _run(env, action):
	if action == 'build':
		build.run(env)
	else:
		raise EnvError("invalid action %s" % action)
