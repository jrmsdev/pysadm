# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from _sadm import log
from _sadm.devops.wapp import cfg
from _sadm.devops.wapp.auth import WebappAuth, AuthError
from _sadm.devops.wapp.errors import error
from _sadm.devops.wapp.session import session
from _sadm.devops.wapp.tpl import tpl

__all__ = ['login', 'loginPost']

def login():
	req = bottle.request
	resp = bottle.response
	auth = WebappAuth(cfg.config)
	sessid = session.cookie(req)
	if not sessid:
		session.new(resp)
	else:
		try:
			auth.check(req)
		except AuthError:
			# if there was an auth error we show the login form
			pass
		else:
			# else we redirect to user home page
			bottle.redirect('/user')
	return tpl.parse('user/login')

def loginPost():
	req = bottle.request
	auth = WebappAuth(cfg.config)
	sessid = session.cookie(req)
	if not sessid:
		log.error('session cookie not found')
		bottle.redirect('/user/login')
	username = req.forms.get('username')
	password = req.forms.get('password')
	if not username:
		return error(401, 'username not provided')
	if not password:
		return error(401, 'user password not provided')
	try:
		auth.login(sessid, username, password)
		log.debug('login done')
	except AuthError as err:
		return error(401, str(err))
	log.debug('redirect')
	bottle.redirect('/')
