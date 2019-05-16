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
		prof = self.profile.name()
		if not self.name in config.listEnvs(prof):
			raise EnvError("%s env not found" % self.name)
		opt = "env.%s" % self.name
		self.cfgfile = config.get(prof, opt)
