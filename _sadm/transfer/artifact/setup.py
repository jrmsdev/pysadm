# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from _sadm import libdir
from _sadm.errors import BuildError
from _sadm.transfer import utils

__all__ = ['cargo', 'artifact']

def cargo(env):
	env.debug('cargo')
	return {}

def artifact(env):
	env.debug('artifact')
	return libdir.fpath('setup', 'transfer', 'artifact.py')
