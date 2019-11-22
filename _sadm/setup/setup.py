# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import makedirs

from _sadm.transfer import extractor

__all__ = ['EnvSetup', 'run']

class EnvSetup(object):

	def __init__(self, env):
		self.__env = env

	@property
	def env(self):
		return self.__env

def run(env):
	env.debug('run')
	s = EnvSetup(env)
	fn = _build(s)
	env.log("setup %s" % fn)
	return 127

def _build(s):
	s.env.debug('build')
	makedirs(s.env.build.rootdir(), exist_ok = True)
	return extractor.gen(s.env, 'setup')
