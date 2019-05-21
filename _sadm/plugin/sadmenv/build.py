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
	env.log("%s.tar" % env.name())
	rdir = builddir.fpath(env, '.')
	fn = builddir.fpath(env, env.name(), meta = True)
	make_archive(fn, 'tar', root_dir = rdir, base_dir = '.', verbose = 1)

def _zip(env):
	env.log("%s.zip" % env.name())
	rdir = builddir.fpath(env, '.', meta = True)
	fn = builddir.fpath(env, '.')
	make_archive(fn, 'zip', root_dir = rdir, base_dir = '.', verbose = 1)

def _meta(env):
	env.log('meta.json')
	with builddir.create(env, 'meta.json', meta = True) as fh:
		json.dump(_getmeta(env), fh, indent = '\t', sort_keys = True)

def _getmeta(env):
	return {
		'sadm.version': env.session.get('sadm.version'),
		'os.platform': env.session.get('os.platform'),
	}
