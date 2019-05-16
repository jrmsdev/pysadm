# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log, config
from _sadm.errors import EnvError
from _sadm.env.profile import Profile

class Env(object):
	name = None
	profile = None
	cfgfile = None

	def __init__(self, profile, name):
		self.name = name
		self.profile = Profile(profile)
		self._load()

	def _load(self):
		if not self.name in config.listEnvs(self.profile.name):
			raise EnvError("%s env not found" % self.name)
		opt = "env.%s" % self.name
		self.cfgfile = config.get(self.profile.name, opt)
