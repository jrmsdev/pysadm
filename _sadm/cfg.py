# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path
from configparser import ConfigParser

_cfgFile = path.expanduser('~/.config/sadm.cfg')
_readFiles = [_cfgFile]

def new():
	config = ConfigParser(
		strict = True,
		default_section = 'default',
		empty_lines_in_values = False,
		comment_prefixes = ('#', ),
		delimiters = ('=', ),
	)
	config.read(_readFiles, encoding = 'utf-8')
	return config
