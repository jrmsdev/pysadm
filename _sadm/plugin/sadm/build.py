# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path, makedirs, unlink

__all__ = ['pre_build', 'build', 'post_build']

_builddir = path.join('.', 'build')

def pre_build(env):
	env.debug('pre_build')
	builddir = path.realpath(_builddir)
	builddir = path.join(builddir, env.profile(), env.name())
	makedirs(builddir, exist_ok = True)
	env.log("build dir %s" % builddir)
	env.session.set('builddir', builddir)
	_lock(env)

def build(env):
	env.debug('build')

def post_build(env):
	env.debug('post_build')
	_saveSession(env)
	_writeSettings(env)
	_unlock(env)

def _lock(env):
	lockfn = path.join(env.session.get('builddir'), '.lock')
	env.debug("lockfn %s" % lockfn)
	env.session.set('lockfn', lockfn)
	try:
		fh = open(lockfn, 'x')
		fh.write('1')
		fh.flush()
		fh.close()
	except FileExistsError as err:
		raise env.error("%s" % err)

def _unlock(env):
	lockfn = env.session.get('lockfn')
	env.debug('session stop')
	env.session.stop()
	try:
		env.debug("lockfn %s" % lockfn)
		unlink(lockfn)
	except FileNotFoundError as err:
		raise env.error("%s" % err)

def _saveSession(env):
	fn = path.join(env.session.get('builddir'), 'session.json')
	env.log("save %s" % fn)
	fn = path.realpath(fn)
	if path.isfile(fn):
		unlink(fn)
	with open(fn, 'x') as fh:
		env.session.dump(fh)

def _writeSettings(env):
	fn = path.join(env.session.get('builddir'), 'configure.ini')
	freal = path.realpath(fn)
	dst = path.dirname(freal)
	makedirs(dst, exist_ok = True)
	if path.isfile(freal):
		unlink(freal)
	with open(freal, 'x') as fh:
		env.settings.write(fh)
	env.log("%s done" % fn)
