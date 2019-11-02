# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sqlite3

from _sadm import log
from _sadm.utils import path, sh

__all__ = ['SessDB']

_sessTable = """CREATE TABLE IF NOT EXISTS sess (
	pk INTEGER PRIMARY KEY AUTOINCREMENT,
	id TEXT NOT NULL UNIQUE,
	user TEXT NOT NULL
);
"""
_sessGet = 'SELECT pk, id, user FROM sess WHERE id = ?;'

class SessDB(object):
	_uri = None
	_mem = False
	_dir = None
	_fn = None

	def __init__(self, config):
		dbdir = config.get('devops', 'session.dbdir',
			fallback = path.join('~', '.local', 'sadm', 'devops', 'wapp'))
		if dbdir == ':memory:':
			self._uri = 'file:session.db?mode=memory&cache=shared'
			self._mem = True
		else:
			self._fn = path.join(dbdir, 'session.db')
			self._uri = "file:%s?cache=shared" % self._fn
		self._dir = dbdir

	def _connect(self):
		log.debug('db connect')
		return sqlite3.connect(self._uri)

	def create(self):
		if self._mem:
			self._mkdb()
		else:
			sh.makedirs(self._dir, exists_ok = True)
			with sh.lockd(self._dir):
				# ~ if path.isfile(self._fn):
					# ~ log.debug("unlink %s" % self._fn)
					# ~ path.unlink(self._fn)
				self._mkdb()

	def _mkdb(self):
		log.debug("create database %s" % self._uri)
		with self._connect() as db:
			db.execute(_sessTable)
			db.commit()

	def check(self, sessid):
		with self._connect() as db:
			cur = db.execute(_sessGet, (sessid,))
			return cur.fetchone()
