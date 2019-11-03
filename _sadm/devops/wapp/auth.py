# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle
from hashlib import sha256

from _sadm import log
from _sadm.devops.wapp.session.session import WebappSession
from _sadm.devops.wapp.user import WebappUser

__all__ = ['WebappAuth', 'AuthError']

class AuthError(Exception):
	pass

class WebappAuth(object):
	_auth = None

	def __init__(self, config):
		self.sess = WebappSession()
		typ = config.get('devops', 'auth', fallback = 'config')
		log.debug("init %s manager" % typ)
		if typ == 'config':
			self._auth = _authConfig(config)
		else:
			raise RuntimeError("invalid auth type: %s" % typ)

	def check(self, req):
		sess = self.sess.check(req)
		if not sess:
			raise AuthError('user session not found')
		return WebappUser(sess['user'], sess = sess)

	def error(self):
		return self._auth.error()

	def login(self, sessid, username, password):
		log.info("user login: %s" % username)
		self._auth.login(username, password)
		sess = self.sess.save(sessid, username)
		user = WebappUser(username, sess = sess)
		return user

class _authConfig(object):

	def __init__(self, cfg):
		if not cfg.has_section('devops.auth'):
			cfg.add_section('devops.auth')
		self.cfg = cfg['devops.auth']

	def error(self):
		log.info('login redirect')
		bottle.redirect('/user/login')

	def login(self, username, password):
		p = self.cfg.get(username, fallback = None)
		if p is None:
			raise AuthError("invalid username: %s" % username)
		h = sha256(password.encode('utf-8'))
		if h.hexdigest() != p:
			raise AuthError("user %s: invalid password" % username)
