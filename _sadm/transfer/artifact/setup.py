# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from _sadm.errors import BuildError
from _sadm.setup.artifact import transfer
from _sadm.transfer import utils

__all__ = ['cargo', 'artifact']

def cargo(env):
	env.debug('cargo')
	# ~ base = path.normpath(env.build.rootdir())
	return {}

def artifact(env):
	env.debug('artifact')
	fn = transfer.gen(env)
	return utils.load(env, fn)
