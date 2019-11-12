# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from secrets import token_urlsafe, token_hex

from _sadm.devops.wapp.session import session

def test_secret_token(devops_wapp):
	assert session._secret is None
	wapp = devops_wapp()
	with wapp.mock() as ctx:
		assert isinstance(session._secret, str)
		x = token_hex(session._tokenSize)
		# check we have the correct size on database VARCHAR for the session id
		assert len(x) == session._tokenSize * 2

def test_new(devops_wapp):
	wapp = devops_wapp()
	with wapp.mock() as ctx:
		resp = ctx.mock.resp
		session.new(resp, sid = 'testing')
		resp.set_cookie.assert_called_with('sadm_devops_session', 'testing',
			secret = session._secret, path = '/', httponly = True)
