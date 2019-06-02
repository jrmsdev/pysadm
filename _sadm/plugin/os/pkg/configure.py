# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import dist
from _sadm.env.settings import Settings

__all__ = ['configure']

def _optfilter(opt):
	dn = dist.getname()
	l = ('update', 'install', 'remove', 'prune')
	if opt in l:
		return opt
	elif opt.startswith(dn + '.'):
		for x in l:
			n = '.' + x
			if opt.endswith(n):
				return opt
	return None

def configure(env, cfg):
	env.settings.merge(cfg, 'os.pkg', _optfilter)
