# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from secrets import token_urlsafe

from _sadm import log

__all__ = ['WebappSession']

class WebappSession(object):
	__secret = token_urlsafe()

	def check(self, req):
		log.debug('check')
		return req.get_cookie('sadm.devops.session', secret = self.__secret)
