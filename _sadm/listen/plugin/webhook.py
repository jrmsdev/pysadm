# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import response

from _sadm import log

__all__ = ['WebhookPlugin']

class WebhookPlugin(object):
	name = 'sadm.webhook'

	def setup(self, wapp):
		log.debug('setup')

	def apply(self, callback, ctx):
		log.debug("ctx: %s - %s" % (type(ctx), ctx))
		if ctx['rule'].startswith('/hook/'):
			log.debug('apply')
			def wrapper(*args, **kwargs):
				log.debug('apply.wrapper')
				resp = callback(*args, **kwargs)
				response.headers['Content-Type'] = 'text/plain; charset=UTF-8'
				return resp
			return wrapper
		log.debug("ignore rule: %s" % ctx['rule'])
		return callback
