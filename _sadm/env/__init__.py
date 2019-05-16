# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log, config
from _sadm.errors import EnvError
from _sadm.env.profile import Profile

class Env(object):
	_name = None
	_cfgfile = None
	_profile = None
	_profName = None

	def __init__(self, profile, name):
		self._name = name
		self._profile = Profile(profile)
		self._profName = self._profile.name()
		self._load()

	def _load(self):
		if not self._name in config.listEnvs(self._profName):
			raise EnvError("%s env not found" % self._name)
		opt = "env.%s" % self._name
		self._cfgfile = config.get(self._profName, opt)

	def name(self):
		return self._name

	def _log(self, func, msg):
		return func("%s/%s %s" % (self._profName, self._name, msg))

	def log(self, msg):
		self._log(log.msg, msg)

	def warn(self, msg):
		self._log(log.warn, msg)

	def debug(self, msg):
		self._log(log.debug, msg)

	def error(self, msg):
		self._log(log.error, msg)
		raise EnvError(msg)
