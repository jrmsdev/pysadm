# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from .check import check

__all__ = ['deploy']

def deploy(env):
	env.log('os user')
	check(env)
