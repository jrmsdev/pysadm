# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log, config
from _sadm.errors import ProfileError

class Profile(object):
	name = None

	def __init__(self, name):
		self.name = name
		self._load()

	def _load(self):
		if not config.has_section(self.name):
			raise ProfileError("%s profile not found" % self.name)
