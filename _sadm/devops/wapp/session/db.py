# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sqlite3

from datetime import datetime

from _sadm import log
from _sadm.utils import path, sh

__all__ = ['SessionDB']

_detectTypes = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES

_sessTable = """
CREATE TABLE IF NOT EXISTS sess (
	pk INTEGER PRIMARY KEY,
	id VARCHAR(128) NOT NULL UNIQUE,
	user VARCHAR(1024) NOT NULL UNIQUE,
	last timestamp
);
"""
_sessGet = 'SELECT pk, id, user, last FROM sess WHERE id = ?;'
_sessLast = 'UPDATE sess SET last = ? WHERE id = ?;'
_sessSave = """
INSERT INTO sess (pk, id, user, last)
	VALUES ((SELECT MAX(pk)+1 FROM sess), ?, ?, ?)
	ON CONFLICT (user) DO
		UPDATE SET id = ?, last = ?
	WHERE user = ?;
"""

class SessionDB(object):
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
		log.debug("connect %s" % self._uri)
		conn = sqlite3.connect(self._uri, detect_types = _detectTypes)
		conn.row_factory = sqlite3.Row
		return conn

	def create(self):
		if self._mem:
			self._mkdb()
		else:
			sh.makedirs(self._dir, exists_ok = True)
			with sh.lockd(self._dir):
				self._mkdb()

	def _mkdb(self):
		with self._connect() as db:
			db.execute(_sessTable)
			db.commit()

	def get(self, sessid, update = False):
		row = None
		with self._connect() as db:
			cur = db.execute(_sessGet, (sessid,))
			row = cur.fetchone()
			if row and update:
				ts = datetime.now()
				db.execute(_sessLast, (ts, sessid))
				db.commit()
				row = dict(row)
				row['last'] = ts
		return row

	def save(self, sessid, username, ts):
		pk = None
		with self._connect() as db:
			cur = db.execute(_sessSave,
				(sessid, username, ts, sessid, ts, username))
			db.commit()
			pk = cur.lastrowid
		if pk is None:
			r = self.get(sessid)
			pk = r['pk']
		return pk
