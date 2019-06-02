# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__all__ = ['deploy']

def check(env):
	env.log('check')

def deploy(env):
	env.log('os user')
	check(env)
