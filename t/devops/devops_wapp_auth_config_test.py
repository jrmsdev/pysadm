# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.devops.wapp.auth import auth
from _sadm.devops.wapp.user import WebappUser

def test_login_config(devops_wapp):
	wapp = devops_wapp('auth')
	with wapp.mock() as ctx:
		wa = auth.WebappAuth(ctx.config)
		sess, req = wapp.mock_sess(wa, '01234567', user = 'tuser')
		u = wa.login(req, '01234567')
		assert isinstance(u, WebappUser)
		assert u.name == 'tuser'
