# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log

__all__ = ['WebhookPlugin']

class WebhookPlugin(object):
	api = 2
	name = 'sadm.webhook'
	__wapp = None

	def setup(self, wapp):
		log.debug('setup')
		self.__wapp = wapp

	def apply(self, callback, ctx):
		if ctx.rule.startswith('/hook/'):
			log.debug("apply for rule: %s" % ctx.rule)
			def wrapper(*args, **kwargs):
				log.debug('apply.wrapper')
				resp = callback(*args, **kwargs)
				self.__wapp.response.headers['Content-Type'] = 'text/plain; charset=UTF-8'
				return resp
			return wrapper
		log.debug("ignore rule: %s" % ctx.rule)
		return callback
