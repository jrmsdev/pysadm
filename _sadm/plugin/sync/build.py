# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import dist
from _sadm.plugin.utils import builddir

from .configure import getInfo

__all__ = ['build']

def build(env):
	dn = dist.getname() + '.'
	for opt in env.settings['sync']:
		if not opt.startswith(dn):
			continue
		inf = getInfo(env.settings, opt)
		_sync(env, inf['cfg.opt'], inf['src'], inf['dst'])
	for inf in env.session.get('sync'):
		_sync(env, inf['cfg.opt'], inf['src'], inf['dst'])

def _sync(env, opt, src, dst):
	if env.assets.isdir(src):
		env.log("%s dir %s -> %s" % (opt, src, dst))
		builddir.sync(env, src, dst)
	else:
		env.log("%s file %s -> %s" % (opt, src, dst))
		with env.assets.open(src) as sfh:
			with builddir.create(env, dst) as dfh:
				dfh.write(sfh.read())