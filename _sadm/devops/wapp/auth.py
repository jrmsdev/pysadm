# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from hashlib import sha256

from _sadm import log
from _sadm.devops.wapp.session.session import WebappSession
from _sadm.devops.wapp.user import WebappUser
from _sadm.devops.wapp.view import view

__all__ = ['WebappAuth', 'AuthError']

class AuthError(Exception):
	pass

class WebappAuth(object):
	_auth = None

	def __init__(self, config):
		self.sess = WebappSession()
		self.type = config.get('devops', 'auth', fallback = 'config')
		if not config.has_section('devops.auth'):
			config.add_section('devops.auth')
		log.debug("init %s manager" % self.type)
		if self.type == 'config':
			self._auth = _authConfig(config)
		elif self.type == 'sslcert':
			self._auth = _authSSLCert(config)
		else:
			raise RuntimeError("invalid auth type: %s" % typ)

	def check(self, req):
		sess = self.sess.check(req)
		if not sess:
			raise AuthError('user session not found')
		return WebappUser(sess.user, sess = sess)

	def error(self):
		log.info('login error, redirect to user login page')
		bottle.redirect(view.url('user.login'))

	def login(self, req, sessid):
		username = self._auth.login(req)
		if not username:
			err = AuthError('could not get the username')
			log.debug("%s" % err)
			raise err
		sess = self.sess.save(sessid, username)
		log.info("user login: %s" % username)
		return WebappUser(username, sess = sess)

# auth users from config file

class _authConfig(object):

	def __init__(self, cfg):
		self.cfg = cfg['devops.auth']

	def login(self, req):
		log.debug('login')
		username = req.forms.get('username')
		password = req.forms.get('password')
		if not username:
			raise bottle.HTTPError(401, 'username not provided')
		if not password:
			raise bottle.HTTPError(401, 'user password not provided')
		p = self.cfg.get(username, fallback = None)
		if p is None:
			raise AuthError("invalid username: %s" % username)
		h = sha256(password.encode('utf-8'))
		if h.hexdigest() != p:
			raise AuthError("user %s: invalid password" % username)
		return username

# auth users using an ssl client certificate via an https proxy

class _authSSLCert(object):

	def __init__(self, cfg):
		self.cfg = cfg['devops']
		self.auth = cfg['devops.auth']
		self._header = self.cfg.get('auth.header', fallback = 'X-Client-Fingerprint')
		self._tokenHeader = self.cfg.get('auth.token.header', fallback = 'X-Auth-Token')

	def _digest(self, s):
		h = sha256(s.encode('utf-8'))
		return h.hexdigest()

	def check(self, req):
		log.debug('check sslcert')
		# https scheme
		scheme = req.headers.get('X-Forwarded-Proto', 'none')
		if scheme != 'https':
			raise AuthError('auth request not from an ssl proxy')
		# auth token from request headers
		htok = req.headers.get(self._tokenHeader, None)
		if htok is None:
			raise AuthError('auth token not found')
		htok = self._digest(htok.strip())
		# check token from config
		tok = self.cfg.get('auth.token', fallback = None)
		if tok is None:
			raise AuthError('auth token not configured')
		tok = tok.strip()
		if htok != tok:
			log.debug("header token: %s" % htok)
			raise AuthError('invalid auth token')
		# get user identification from request headers
		uid = req.headers.get(self._header, None)
		if uid is None:
			raise AuthError('auth user id not found')
		return uid

	def login(self, req):
		log.debug('login sslcert')
		username = req.forms.get('username')
		if not username:
			raise bottle.HTTPError(401, 'username not provided')
		uid = self.check(req)
		x = self.auth.get(username, fallback = None)
		if x is None:
			raise AuthError("invalid username: %s" % username)
		uid = self._digest(uid.strip())
		if x != uid:
			raise AuthError("user %s: invalid id" % username)
		return username
