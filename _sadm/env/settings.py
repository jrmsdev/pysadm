# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from collections import deque
from configparser import ConfigParser, ExtendedInterpolation
from configparser import NoOptionError, ParsingError

from _sadm.configure import pluginsList, getPlugin
from _sadm.errors import SettingsError

__all__ = ['Settings']

_unset = object()

class Settings(ConfigParser):

	def __init__(self):
		super().__init__(defaults = {},
			allow_no_value = False,
			delimiters = ('=',),
			comment_prefixes = ('#',),
			strict = True,
			interpolation = ExtendedInterpolation(),
			default_section = 'default')

	def plugins(self, action, revert = False):
		for p in pluginsList(revert = revert):
			if self.has_section(p):
				yield (p, getPlugin(p, action))

	def read_file(self, fh):
		try:
			super().read_file(fh)
		except ParsingError as err:
			raise SettingsError(str(err))

	def getlist(self, section, option, fallback = _unset):
		try:
			if fallback is _unset:
				s = super().get(section, option)
			else:
				s = super().get(section, option, fallback = '')
				if s == '':
					return fallback
		except NoOptionError as err:
			raise SettingsError(str(err))
		l = deque()
		for val in s.split():
			val = val.strip()
			for val2 in val.split(','):
				val2 = val2.strip()
				if val2 != '':
					l.append(val2)
		return tuple(l)
