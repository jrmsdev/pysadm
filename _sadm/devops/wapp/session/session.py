# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from secrets import token_urlsafe, token_hex

from _sadm import log
from _sadm.devops.wapp import cfg
from _sadm.devops.wapp.session.db import SessionDB

__all__ = ['WebappSession', 'init', 'check', 'new']

_secret = None
_tokenSize = 64

class WebappSession(object):
	name = 'sadm_devops_session'
	_id = None

	def __init__(self):
		self._db = SessionDB(cfg.config)

	def cookie(self, req):
		log.debug('get cookie')
		if _secret is None:
			raise RuntimeError('session module not initialized')
		self._id = req.get_cookie(self.name, secret = _secret)
		return self._id

	def check(self, req):
		log.debug('check')
		self.cookie(req)
		if self._id is not None:
			row = self._db.get(self._id)
			if row:
				return dict(row)
		return None

	def save(self, sessid, username):
		self._id = sessid
		self._db.save(self._id, username)
		return {'id': self._id, 'user': username}

def init(config):
	global _secret
	_secret = token_urlsafe(_tokenSize)
	log.debug('init')
	db = SessionDB(config)
	db.create()

def cookie(req):
	return WebappSession().cookie(req)

def new(resp):
	if _secret is None:
		raise RuntimeError('session module not initialized')
	s = WebappSession()
	sid = token_hex(_tokenSize)
	resp.set_cookie(s.name, sid, secret = _secret, path = '/', httponly = True)