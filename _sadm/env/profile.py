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
		found = None
		for s in config.sections():
			if s.startswith('profile.'):
				n = '.'.join(s.split('.')[1:])
				if self.name == n:
					found = n
					break
		if found is None:
			raise ProfileError("%s profile not found" % self.name)
