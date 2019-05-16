# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log, config
from _sadm.errors import EnvError
from _sadm.env.profile import Profile

class Env(object):
	_name = None
	_cfgfile = None
	_profile = None

	def __init__(self, profile, name):
		self._name = name
		self._profile = Profile(profile)
		self._load()

	def _load(self):
		prof = self._profile.name()
		if not self._name in config.listEnvs(prof):
			raise EnvError("%s env not found" % self._name)
		opt = "env.%s" % self._name
		self._cfgfile = config.get(prof, opt)

	def name(self):
		return self._name
