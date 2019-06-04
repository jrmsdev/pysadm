# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__all__ = ['configure']

def configure(env, cfg):
	for opt in cfg['sync']:
		env.session.set(opt, cfg.getlist('sync', opt))
