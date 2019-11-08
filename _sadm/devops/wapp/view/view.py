# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.devops.wapp.static import static
from _sadm.devops.wapp.view import index, view
from _sadm.devops.wapp.view.user import auth

__all__ = ['url']

reg = (
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

__idx = None
if __idx is None:
	__idx = {}
	for h in reg:
		name = h[0]
		cfg = h[1]
		__idx[name] = cfg

def url(view, **kw):
	cfg = __idx.get(view, None)
	if cfg is None:
		raise RuntimeError("invalid view name: %s" % view)
	u = cfg.get('url', None)
	if u is None:
		return cfg['route']
	return u.format(**kw)
