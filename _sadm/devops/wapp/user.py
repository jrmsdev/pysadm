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

	def check(self, req):
		log.debug('check')
		sessid = self._sess.check(req)
		if sessid:
			pass
		else:
			log.debug('session not found')
			raise UserAuthError('session not found')
