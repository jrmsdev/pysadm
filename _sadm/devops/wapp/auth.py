# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from _sadm import log
from _sadm.devops.wapp.sess import WebappSession
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

	def error(self):
		return self._auth.error()

	def check(self, req):
		sess = self.sess.check(req)
		if not sess:
			raise AuthError('user session not found')
		user = WebappUser(sess.user, sess = sess)
		user.check(req)
		return user

class _authConfig(object):

	def __init__(self, cfg):
		pass

	def error(self):
		log.info('login redirect')
		bottle.redirect('/user/login')
