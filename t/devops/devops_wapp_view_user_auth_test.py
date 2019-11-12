# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from contextlib import contextmanager
from pytest import raises
from unittest.mock import Mock

from _sadm.devops.wapp.view import view
from _sadm.devops.wapp.view.user import auth

@contextmanager
def mock_session(wapp):
	bup = Mock()
	bup.session = auth.session
	with wapp.mock() as ctx:
		try:
			ctx.session = ctx.mock.session
			ctx.session.cookie.return_value = '01234567'
			auth.session = ctx.session
			ctx.auth = ctx.mock.auth
			yield ctx
		finally:
			del auth.session
			auth.session = bup.session

def test_login(devops_wapp):
	wapp = devops_wapp()
	with wapp.mock() as ctx:
		ctx.auth = ctx.mock.auth
		auth.login(auth = ctx.auth)
		ctx.tpl.parse.assert_called_with('user/login', auth = ctx.auth)
		assert ctx.auth.mock_calls == []

def test_auth_check(devops_wapp):
	wapp = devops_wapp()
	with mock_session(wapp) as ctx:
		with raises(bottle.HTTPResponse) as resp:
			auth.login(auth = ctx.auth)
		wapp.checkRedirect(resp, 302, view.url('index'))
		req = bottle.request
		resp = bottle.response
		ctx.auth.check.assert_called_with(req)
		assert ctx.tpl.parse.mock_calls == []
		ctx.session.cookie.assert_called_with(req)
		assert ctx.session.new.mock_calls == []
