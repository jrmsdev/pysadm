# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import response

from _sadm import log

__all__ = ['WebhookPlugin']

class WebhookPlugin(object):

	def setup(self, wapp):
		log.debug('setup')

	def apply(self, callback, ctx):
		log.debug('apply')
		def wrapper(*args, **kwargs):
			log.debug('apply.wrapper')
			resp = callback(*args, **kwargs)
			response.headers['Content-Type'] = 'text/plain; charset=UTF-8'
			return resp
		return wrapper
