# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from _sadm import log
from _sadm.devops.wapp import cfg
from _sadm.devops.wapp.auth import WebappAuth, AuthError
from _sadm.devops.wapp.errors import error
from _sadm.devops.wapp.session import session
from _sadm.devops.wapp.tpl import tpl

__all__ = ['login']

def login():
	req = bottle.request
	resp = bottle.response
	auth = WebappAuth(cfg.config)
	sessid = session.cookie(req)
	if req.method == 'POST':
		if not sessid:
			return error(400, 'session cookie not found')
		username = req.forms.get('username')
		password = req.forms.get('password')
		if not username:
			return error(400, 'username not provided')
		if not password:
			return error(400, 'user password not provided')
		try:
			auth.login(req, username, password)
			log.debug('login done')
		except AuthError as err:
			return error(400, str(err))
		log.debug('redirect')
		bottle.redirect('/')
	else:
		if not sessid:
			session.new(resp)
		else:
			try:
				auth.check(req)
			except AuthError:
				pass
			else:
				bottle.redirect('/user')
	return tpl.parse('user/login')
