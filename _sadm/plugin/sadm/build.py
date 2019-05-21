# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.plugin.utils import builddir

__all__ = ['pre_build', 'post_build']

def pre_build(env):
	builddir.lock(env)
	_writeSettings(env)

#def build(env):
#	env.log('build')

def post_build(env):
	_saveSession(env)
	builddir.unlock(env)

def _saveSession(env):
	env.log('save session.json')
	with builddir.create(env, 'session.json', meta = True) as fh:
		env.session.dump(fh)

def _writeSettings(env):
	with builddir.create(env, 'configure.ini', meta = True) as fh:
		env.settings.write(fh)
	env.log('configure.ini done')
