# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from pytest import raises

from _sadm.devops.wapp.auth import auth
from _sadm.devops.wapp.auth.error import AuthError
from _sadm.devops.wapp.user import WebappUser

def test_login_sslcert(devops_wapp):
	wapp = devops_wapp('auth.sslcert')
	with wapp.mock() as ctx:
		wa = auth.WebappAuth(ctx.config)
		sess, req = wapp.mock_sess(wa, '01234567', user = 'testing')
		u = wa.login(req, '01234567')
		assert isinstance(u, WebappUser)
		assert u.name == 'testing'
