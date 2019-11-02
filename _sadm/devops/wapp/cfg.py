# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from configparser import ConfigParser, ExtendedInterpolation

__all__ = ['config', 'new']

config = None

def new(fn):
	global config
	config = ConfigParser(
		defaults = None,
		allow_no_value = False,
		delimiters = ('=',),
		comment_prefixes = ('#',),
		strict = True,
		interpolation = ExtendedInterpolation(),
		default_section = 'default',
	)
	with open(fn, 'r') as fh:
		config.read_file(fh)
	return config
