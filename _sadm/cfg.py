# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path
from configparser import ConfigParser

_readFiles = [path.expanduser('~/.config/sadm.cfg')]

def new():
	config = ConfigParser()
	config.read(_readFiles, encoding = 'utf-8')
	return config
