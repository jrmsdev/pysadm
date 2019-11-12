# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from pytest import raises
from unittest.mock import Mock

from _sadm.devops.wapp.auth import auth
from _sadm.devops.wapp.auth.config import AuthConfig
from _sadm.devops.wapp.user import WebappUser
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

def _newreq(sessid):
	req = Mock()
	req.get_cookie.return_value = sessid
	return req

def _newsess(wa, sessid):
	wa.sess.save(sessid, 'testing')
	return _newreq(sessid)

def test_user(devops_wapp):
	wapp = devops_wapp('auth')
	with wapp.mock() as ctx:
		wa = auth.WebappAuth(ctx.config)
		req = _newsess(wa, '01234567')
		u = wa.check(req)
		assert isinstance(u, WebappUser)
		assert u.name == 'testing'
		assert u.sess.id == '01234567'
		assert u.sess.user == 'testing'
