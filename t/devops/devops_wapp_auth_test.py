# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from pytest import raises

from _sadm.devops.wapp.auth import auth
from _sadm.devops.wapp.auth.config import AuthConfig
from _sadm.devops.wapp.view import view

def test_init(devops_wapp):
	wapp = devops_wapp('auth')
	with wapp.mock() as ctx:
		wa = auth.WebappAuth(ctx.config)
		assert isinstance(wa._auth, AuthConfig)

def test_init_error(devops_wapp):
	wapp = devops_wapp('auth')
	with wapp.mock() as ctx:
		ctx.config.set('devops', 'auth', 'testing.invalid')
		with raises(RuntimeError, match = 'invalid auth type: testing.invalid'):
			auth.WebappAuth(ctx.config)

def test_error(devops_wapp):
	wapp = devops_wapp('auth')
	with wapp.mock() as ctx:
		wa = auth.WebappAuth(ctx.config)
		with raises(bottle.HTTPResponse) as exc:
			wa.error()
		wapp.checkRedirect(exc, 302, view.url('user.login'))
