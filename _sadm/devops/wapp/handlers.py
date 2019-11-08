# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log
from _sadm.devops.wapp.static import static
from _sadm.devops.wapp.view import index
from _sadm.devops.wapp.view.user import auth

__all__ = ['init', 'url']

_reg = (
	('static', {
		'route': r'/static/<filename:re:.*\..*>',
		'view': static.serve,
		'skip': ['sadm.devops.auth'],
		'url': '/static/{filename}',
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
_regidx = {}

def init(wapp):
	idx = 0
	for h in _reg:
		name = h[0]
		cfg = h[1]
		wapp.route(cfg['route'], cfg.get('method', 'GET'), cfg['view'],
			name = name, skip = cfg.get('skip', []))
		_regidx[name] = cfg

def url(view, **kw):
	cfg = _regidx.get(view, None)
	if cfg is None:
		raise RuntimeError("invalid view name: %s" % view)
	u = cfg.get('url', None)
	if u is None:
		return cfg['route']
	return u.format(**kw)
