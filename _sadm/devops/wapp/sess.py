# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sqlite3

from secrets import token_urlsafe

from _sadm import log
from _sadm.utils import path, sh

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
	_db = _sessDB(config)

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

_sessTable = """CREATE TABLE sess (
	pk INTEGER PRIMARY KEY AUTOINCREMENT,
	id TEXT NOT NULL UNIQUE,
	user TEXT NOT NULL
);
"""
_sessGet = 'SELECT pk, id, user FROM sess WHERE id = ?;'

class _sessDB(object):
	_db = None

	def __init__(self, config):
		dbdir = config.get('devops', 'session.dbdir',
			fallback = path.join('~', '.local', 'sadm', 'devops', 'wapp'))
		if dbdir == ':memory:':
			self._uri = 'file:session.db?mode=memory&cache=shared'
			self._mkdb()
		else:
			sh.makedirs(dbdir, exists_ok = True)
			fn = path.join(dbdir, 'session.db')
			with sh.lockd(dbdir):
				if path.isfile(fn):
					log.debug("unlink %s" % fn)
					path.unlink(fn)
				self._uri = "file:%s?cache=shared" % fn
				self._mkdb()

	def _connect(self):
		log.debug('db connect')
		self._db = sqlite3.connect(self._uri)

	def _mkdb(self):
		log.debug("create database %s" % self._uri)
		self._connect()
		self._db.execute(_sessTable)
		self._db.commit()

	def close(self):
		self._db.close()

	def check(self, sessid):
		cur = self._db.execute(_sessGet, sessid)
		row = cur.fetchone()
		if row:
			return dict(row)
		return None
