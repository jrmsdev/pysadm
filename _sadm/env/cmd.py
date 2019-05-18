# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import getcwd
from time import strftime, time

from _sadm.errors import EnvError

def run(env, action):
	_start = time()
	env.info("%s start %s" % (action, strftime('%c %z')))
	env.log("%s from %s" % (action, getcwd()))
	env.configure()
	try:
		env.report(action, startTime = _start)
	finally:
		env.info("%s end %s" % (action, strftime('%c %z')))
