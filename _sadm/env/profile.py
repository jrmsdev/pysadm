# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log, config
from _sadm.errors import ProfileError

class Profile(object):
	_name = None

	def __init__(self, name):
		self._name = name
		self._load()

	def _load(self):
		if not config.has_section(self._name):
			raise ProfileError("%s profile not found" % self._name)

	def name(self):
		return self._name
