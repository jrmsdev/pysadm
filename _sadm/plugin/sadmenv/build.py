# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from shutil import make_archive
from _sadm.plugin.utils import builddir

__all__ = ['post_build']

def post_build(env):
	typ = 'tar'
	rdir = builddir.fpath(env, '.')
	fn = builddir.fpath(env, env.name(), meta = True)
	env.log("post_build %s.%s" % (fn, typ))
	make_archive(fn, typ, root_dir = rdir, base_dir = '.', verbose = 1)
