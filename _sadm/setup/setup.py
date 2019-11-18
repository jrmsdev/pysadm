# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__all__ = ['EnvSetup', 'run']

class EnvSetup(object):

	def __init__(self, env):
		self.__env = env

	@property
	def env(self):
		return self.__env

	def transfer(self):
		self.__env.debug('transfer')

def run(env):
	env.debug('run')
	s = EnvSetup(env)
	s.transfer()
	return 127
