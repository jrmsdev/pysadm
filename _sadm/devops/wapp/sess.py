# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from secrets import token_urlsafe

from _sadm import log
from _sadm.devops.wapp.sessdb import SessDB

__all__ = ['init', 'WebappSession']

_db = None
_secret = None

def init(config):
	global _db
	global _secret
	log.debug('init')
	_secret = token_urlsafe()
	if _db is not None:
		log.debug('close previous database connection')
		_db.close()
		_db = None
	_db = SessDB(config)

class WebappSession(object):
	_id = None
	_name = 'sadm_devops_session'

	def check(self, req):
		log.debug('check')
		if _db is None or _secret is None:
			raise RuntimeError('session not initialized')
		self._id = req.get_cookie(self._name, secret = _secret)
		if not self._id:
			return None
		return _db.check(self._id)
