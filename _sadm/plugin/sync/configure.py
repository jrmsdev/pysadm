# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from collections import deque

__all__ = ['configure']

def configure(env, cfg):
	data = deque()
	for opt in cfg['sync']:
		data.append(getInfo(cfg, opt))
	env.session.set('sync', tuple(data))

def getInfo(cfg, opt):
	i = cfg.getlist('sync', opt)
	return {'cfg.opt': opt, 'src': i[0], 'dst': i[1]}
