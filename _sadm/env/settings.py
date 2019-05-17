# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json
from os import path

from _sadm import log, config
from _sadm.errors import EnvError

class Settings(object):
	_profile = None
	_env = None
	_filename = None
	_data = None

	def __init__(self, profile, env, cfgfile):
		self._profile = profile
		self._env = env
		self._filename = self._setFilename(cfgfile)
		self._data = self._load()

	def _setFilename(self, cfgfile):
		pdir = config.get(self._profile, 'dir')
		pdir = pdir.strip()
		if pdir == '':
			err = EnvError("%s profile dir not set" % self._profile)
			log.error(str(err))
			raise err
		return path.join(path.normpath(pdir), cfgfile)

	def _load(self):
		with open(self._filename, 'r') as fh:
			return json.load(fh)
		return {}
