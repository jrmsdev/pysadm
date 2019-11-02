# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sqlite3

from _sadm import log
from _sadm.utils import path, sh

__all__ = ['SessDB']

_sessTable = """CREATE TABLE sess (
	pk INTEGER PRIMARY KEY AUTOINCREMENT,
	id TEXT NOT NULL UNIQUE,
	user TEXT NOT NULL
);
"""
_sessGet = 'SELECT pk, id, user FROM sess WHERE id = ?;'

class SessDB(object):
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
		cur = self._db.execute(_sessGet, (sessid,))
		row = cur.fetchone()
		if row:
			return dict(row)
		return None
