# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json
from shutil import make_archive

from _sadm.plugin.utils import builddir

__all__ = ['post_build']

def post_build(env):
	_tar(env)
	_meta(env)
	_zip(env)

def _tar(env):
	rdir = builddir.fpath(env, '.')
	fn = builddir.fpath(env, env.name(), meta = True)
	make_archive(fn, 'tar', root_dir = rdir, base_dir = '.', verbose = 1)
	env.log("%s.tar done" % fn)

def _zip(env):
	rdir = builddir.fpath(env, '.', meta = True)
	fn = builddir.fpath(env, '.')
	make_archive(fn, 'zip', root_dir = rdir, base_dir = '.', verbose = 1)
	env.log("%s.zip done" % fn)

def _meta(env):
	fn = builddir.fpath(env, 'meta.json', meta = True)
	with builddir.create(env, 'meta.json', meta = True) as fh:
		json.dump({}, fh)
	env.log("%s done" % fn)
