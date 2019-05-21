# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.plugin.utils import builddir

__all__ = ['post_build']

#def build(env):
#	env.log('build')

def post_build(env):
	env.log('post_build')
