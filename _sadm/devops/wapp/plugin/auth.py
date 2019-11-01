# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log

__all__ = ['AuthPlugin']

class AuthPlugin(object):
	api = 2
	name = 'sadm.devops.auth'

	def setup(self, wapp):
		log.debug('setup')

	def apply(self, callback, ctx):
		log.debug("apply for rule: %s" % ctx.rule)
		def wrapper(*args, **kwargs):
			log.debug('apply.wrapper')
			resp = callback(*args, **kwargs)
			return resp
		return wrapper
