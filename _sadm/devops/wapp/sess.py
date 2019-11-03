# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from secrets import token_urlsafe, token_hex

from _sadm import log
from _sadm.devops.wapp import cfg
from _sadm.devops.wapp.sessdb import SessDB

__all__ = ['WebappSession', 'init', 'check', 'new']

_secret = None

class WebappSession(object):
	name = 'sadm_devops_session'
	_id = None

	def __init__(self):
		self._db = SessDB(cfg.config)

	def cookie(self, req):
		log.debug('get cookie')
		if _secret is None:
			raise RuntimeError('session module not initialized')
		self._id = req.get_cookie(self.name, secret = _secret)
		return self._id

	def check(self, req):
		log.debug('check')
		self.cookie()
		if self._id is not None:
			row = self._db.check(self._id)
			if row:
				return dict(row)
		return None

def init(config):
	global _secret
	_secret = token_urlsafe()
	log.debug('init')
	db = SessDB(config)
	db.create()

def cookie(req):
	return WebappSession().cookie(req)

def new(resp):
	if _secret is None:
		raise RuntimeError('session module not initialized')
	s = WebappSession()
	sid = token_hex()
	resp.set_cookie(s.name, sid, secret = _secret, path = '/', httponly = True)
