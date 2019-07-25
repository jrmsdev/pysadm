# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__all__ = ['cfgfilter', 'configure']

def cfgfilter(opt):
	return opt

def configure(env, cfg):
	env.settings.merge(cfg, 'os.pkg', ('update', 'install', 'remove', 'prune'))
