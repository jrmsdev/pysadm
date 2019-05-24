# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path, unlink, makedirs, system
from shutil import rmtree

__all__ = ['lock', 'unlock', 'fpath', 'create']

def lock(env):
	bdir = env.build.rootdir()
	env.log("build dir %s" % bdir)
	fn = path.normpath(bdir) + '.lock'
	env.debug("lock %s" % fn)
	env.session.set('lockfn', fn)
	makedirs(path.dirname(bdir), exist_ok = True)
	try:
		fh = open(fn, 'x')
	except FileExistsError:
		raise env.error("lock file exists: %s" % fn)
	fh.write('1')
	fh.flush()
	fh.close()
	_cleandir(env, bdir)
	env.debug('env.build create')
	env.build.create()

def unlock(env):
	env.debug('env.build close')
	env.build.close()
	fn = env.session.get('lockfn')
	env.debug("unlock %s" % fn)
	try:
		unlink(fn)
	except FileNotFoundError:
		raise env.error("unlock file not found: %s" % fn)

def _cleandir(env, bdir):
	base = path.normpath(bdir)
	bdirs = [
		bdir,
		base + '.meta',
	]
	bfiles = [
		base + '.tar',
		base + '.zip',
		base + '.checksum',
	]
	for d in bdirs:
		if path.isdir(d):
			env.debug("rmtree %s" % d)
			rmtree(d) # clean tree
		makedirs(d) # recreate base dirs
	for f in bfiles:
		if path.isfile(f):
			unlink(f)

def _open(env, filename, mode = 'r', meta = False):
	fn = fpath(env, filename, meta = meta)
	if mode != 'r':
		dstdir = path.dirname(fn)
		if not path.isdir(dstdir):
			env.debug("makedirs %s" % dstdir)
			makedirs(dstdir, exist_ok = True)
	env.debug("open(%s) %s" % (mode, fn))
	return open(fn, mode)

def fpath(env, *parts, meta = False):
	bdir = env.build.rootdir()
	if meta:
		bdir = path.normpath(bdir) + '.meta'
	fn = path.join(*parts)
	fn = path.normpath(fn)
	if fn.startswith(path.sep):
		fn = fn.replace(path.sep, '', 1)
	return path.realpath(path.join(bdir, fn))

def create(env, filename, meta = False):
	fh = _open(env, filename, mode = 'x', meta = meta)
	if not meta:
		env.build.addfile(filename)
	return fh

def sync(env, src, dst):
	srcdir = path.join(env.assets.rootdir(), src)
	dstdir = fpath(env, dst)
	if path.isdir(dstdir):
		rmtree(dstdir)
	makedirs(dstdir)
	system("rsync -ax %s/ %s/" % (srcdir, dstdir))
