# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from collections import deque

__all__ = ['configure']

def configure(env, cfg):
	data = deque()
	for opt in cfg['sync']:
		_configure(data, cfg, opt)
	env.session.set('sync', tuple(data))

def _configure(data, cfg, opt):
	i = cfg.getlist('sync', opt)
	data.append({'src': i[0], 'dst': i[1]})
