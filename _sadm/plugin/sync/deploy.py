# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import tarfile
from os import stat

from _sadm.utils import path

__all__ = ['deploy']

# run as root at first pass
sumode = 'pre'

def deploy(env):
	fn = env.name() + '.tar'
	fpath = env.assets.rootdir(env.name(), fn)
	mtime = stat(fpath).st_mtime
	target = env.settings.get('sadmenv', 'target.dir')
	env.log("%s %s" % (fn, mtime))
	env.log("target %s" % target)
	with open(fpath, 'rb') as fh:
		tar = tarfile.open(fn, 'r:', fileobj = fh)
		try:
			for tinfo in tar:
				tinfo.mtime = mtime
				dst = path.join(target, tinfo.name)
				if _syncTarget(env, dst, tinfo):
					env.log("  %s" % tinfo.name)
					tar.extract(tinfo, path = target, set_attrs = True)
				else:
					env.debug("  %s OK" % tinfo.name)
		finally:
			tar.close()

def _syncTarget(env, dst, tinfo):
	env.debug("check target %s" % dst)
	try:
		mtime = stat(dst).st_mtime
	except FileNotFoundError:
		return True
	return mtime < tinfo.mtime
