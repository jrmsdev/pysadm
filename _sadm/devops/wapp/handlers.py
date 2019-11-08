# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log
from _sadm.devops.wapp.static import static
from _sadm.devops.wapp.view import index
from _sadm.devops.wapp.view.user import auth

__all__ = ['init']

_reg = (
	('static', {
		'route': r'/static/<filename:re:.*\..*>',
		'view': static.serve,
		'skip': ['sadm.devops.auth'],
	}),
	('index', {
		'route': '/',
		'view': index.handle,
	}),
	('user.login', {
		'route': '/user/login',
		'view': auth.login,
		'skip': ['sadm.devops.auth'],
	}),
	('user.login_post', {
		'route': '/user/login',
		'view': auth.loginPost,
		'method': 'POST',
		'skip': ['sadm.devops.auth'],
	}),
)

def init(wapp):
	for h in _reg:
		name = h[0]
		cfg = h[1]
		wapp.route(cfg['route'], cfg.get('method', 'GET'), cfg['view'],
			name = name, skip = cfg.get('skip', []))
