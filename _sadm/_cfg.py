# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path
from configparser import ConfigParser

from _sadm.errors import ProfileError

_cfgFile = path.realpath('./sadm.cfg')

_DEFAULT = {
	'profile': 'default',
	'env': 'default',
}

class Config(ConfigParser):
	_fn = None

	def reload(self):
		self.read([self._fn], encoding = 'utf-8')

	def listProfiles(self):
		return sorted(self.sections())

	def listEnvs(self, profile):
		if not self.has_section(profile):
			raise ProfileError("%s profile not found" % profile)
		e = {}
		for opt in self.options(profile):
			if opt.startswith('env.'):
				n = '.'.join(opt.split('.')[1:]).strip()
				if n != '':
					e[n] = True
		return sorted(e.keys())

def new():
	config = Config(
		defaults = _DEFAULT,
		strict = True,
		default_section = 'default',
		empty_lines_in_values = False,
		comment_prefixes = ('#', ),
		delimiters = ('=', ),
	)
	config._fn = _cfgFile
	config.reload()
	return config
