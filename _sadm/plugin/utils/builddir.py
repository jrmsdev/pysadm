# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path, unlink, makedirs

__all__ = ['lock']

_builddir = path.join('.', 'build')

def lock(env):
	builddir = path.realpath(_builddir)
	builddir = path.join(builddir, env.profile(), env.name())
	makedirs(builddir, exist_ok = True)
	env.log("build dir %s" % builddir)
	env.session.set('builddir', builddir)
	fn = path.join(builddir, '.lock')
	env.debug("lockfn %s" % fn)
	env.session.set('lockfn', fn)
	try:
		fh = open(fn, 'x')
	except FileExistsError:
		raise env.error("lock file exists: %s" % fn)
	fh.write('1')
	fh.flush()
	fh.close()
	return env

def unlock(env):
	fn = env.session.get('lockfn', default = None)
	if fn is None:
		env.debug('builddir not locked')
	else:
		env.debug("unlock %s" % fn)
		try:
			unlink(fn)
		except FileNotFoundError:
			raise env.error("unlock file not found: %s" % fn)

def _open(env, filename, mode = 'r'):
	builddir = env.session.get('builddir')
	fn = path.normpath(filename)
	if fn.startswith(path.sep):
		fn.replace(path.sep, '', 1)
	fn = path.join(builddir, fn)
	if mode != 'r':
		makedirs(path.dirname(fn), exist_ok = True)
	return open(fn, mode)

def create(env, filename):
	return _open(env, filename, mode = 'x')

def read(env, filename):
	return _open(env, filename, mode = 'r')

def write(env, filename, append = False):
	m = 'w'
	if append:
		m = 'a'
	return _open(env, filename, mode = m)
