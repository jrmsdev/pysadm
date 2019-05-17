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
		self.debug('load')
		if not self._name in config.listEnvs(self._profName):
			self.error('env not found')
		opt = "env.%s" % self._name
		self._cfgfile = config.get(self._profName, opt)
		self._cfgfile = self._cfgfile.strip()
		self._loadcfg()

	def _loadcfg(self):
		if self._cfgfile == '':
			self.error('config file not set')
		self.debug("cfgfile %s" % self._cfgfile)

	def name(self):
		return self._name

	def _log(self, func, msg):
		func("%s/%s %s" % (self._profName, self._name, msg))

	def log(self, msg):
		self._log(log.msg, msg)

	def warn(self, msg):
		self._log(log.warn, msg)

	def debug(self, msg):
		tag = "%s/%s" % (self._profName, self._name)
		log.debug("%s" % msg, depth = 4, tag = tag)

	def error(self, msg):
		self._log(log.error, msg)
		raise EnvError(msg)
