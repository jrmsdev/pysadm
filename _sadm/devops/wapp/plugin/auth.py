# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from _sadm import log
from _sadm.devops.wapp.user import WebappUser, UserAuthError

__all__ = ['AuthPlugin']

class AuthPlugin(object):
	api = 2
	name = 'sadm.devops.auth'

	def __init__(self, config):
		self.config = config

	def setup(self, wapp):
		typ = self.config.get('devops', 'auth', fallback = 'config')
		log.debug("setup %s manager" % typ)
		if typ == 'config':
			self.auth = AuthConfig(self.config)
		else:
			raise RuntimeError("invalid auth type: %s" % typ)

	def apply(self, callback, ctx):
		log.debug("apply for rule: %s" % ctx.rule)
		def wrapper(*args, **kwargs):
			log.debug('apply.wrapper')
			autherr = None
			try:
				log.debug('user auth check')
				user = self.auth.check(bottle.request)
			except UserAuthError as err:
				autherr = err
			if autherr is None:
				resp = callback(*args, **kwargs)
				return resp
			else:
				bottle.redirect('/user/login')
		return wrapper

class AuthConfig(object):
	name = 'config'

	def __init__(self, cfg):
		pass

	def check(self, req):
		user = WebappUser()
		user.auth(req)
		return user
