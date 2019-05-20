# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from time import strftime, time

from _sadm import config
from _sadm.errors import EnvError

__all__ = ['run']

_validAction = {'build': True}

def run(env, action):
	_start = time()
	env.info("%s start %s" % (action, strftime('%c %z')))
	env.log("%s %s" % (config.name(), config.filename()))
	try:
		if not _validAction.get(action, False):
			raise EnvError("invalid action %s" % action)
		with env.lock() as env:
			env.configure()
			_runAction(env, action)
			env.report(action, startTime = _start)
	finally:
		env.info("%s end %s" % (action, strftime('%c %z')))

def _runAction(env, action):
	for p, mod in env.settings.plugins(action):
		tag = "%s.%s" % (action, p)
		env.start(tag)
		func = getattr(mod, action)
		func(env)
		env.end(tag)
