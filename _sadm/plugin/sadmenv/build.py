# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.plugin.utils import builddir

__all__ = ['build', 'post_build']

# ~ def pre_build(env):
	# ~ env.debug('pre_build')

def build(env):
	env.debug('build')

def post_build(env):
	env.debug('post_build')
