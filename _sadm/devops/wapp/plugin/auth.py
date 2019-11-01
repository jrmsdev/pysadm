# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log

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
			resp = callback(*args, **kwargs)
			return resp
		return wrapper

class AuthConfig(object):
	name = 'config'

	def __init__(self, cfg):
		pass
