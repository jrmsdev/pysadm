# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log
from _sadm.devops.wapp.sess import WebappSession

__all__ = ['WebappUser', 'UserAuthError']

class UserAuthError(Exception):
	pass

class WebappUser(object):
	name = None

	def __init__(self):
		self._sess = WebappSession()

	def auth(self, req):
		log.debug('auth')
		sessid = self._sess.check(req)
		if sessid:
			pass
		else:
			log.info('user session not found')
			raise UserAuthError('session not found')
