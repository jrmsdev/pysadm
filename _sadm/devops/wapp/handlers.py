# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log
from _sadm.devops.wapp.view import view

__all__ = ['init']

def init(wapp):
	for h in view.reg:
		name = h[0]
		cfg = h[1]
		wapp.route(cfg['route'], cfg.get('method', 'GET'), cfg['view'],
			name = name, skip = cfg.get('skip', []))
