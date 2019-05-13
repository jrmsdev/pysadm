# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
import sqlite3
from os import path, makedirs

from _sadm import log

_DB_CREATE = """
create table syslog (
	id integer primary key autoincrement,
	time text default current_timestamp,
	level text,
	msg text
);
"""

class _webLogger(object):
	db = None

	def close(self):
		self.db.close()

	def error(self, msg):
		print("[syslog] E:", msg, file = sys.stderr)

	def warn(self, msg):
		print("[syslog] W:", msg, file = sys.stderr)

	def info(self, msg):
		print("[syslog] I:", msg, file = sys.stdout)

	def msg(self, msg):
		print("[syslog]", msg, file = sys.stdout)

_logger = _webLogger()

def init():
	log.debug('init web syslog')
	try:
		_logger.db = _dbInit()
	except Exception as err:
		log.debug("exception: %s" % type(err))
		log.error("could not init web syslog: %s" % err)
	else:
		log.debug('attach child logger')
		log._logger._child = _logger
		log.info('syslog start')

def close():
	if _logger.db is not None:
		log.info('syslog end')
		_logger.close()

_dbfile = path.expanduser('~/.local/sadm/syslog.db')

def _dbInit():
	log.debug("syslog init %s" % _dbfile)
	log.debug("sqlite version %s (lib %s)" % (sqlite3.version, sqlite3.sqlite_version))
	mkdb = not path.isfile(_dbfile)
	if mkdb:
		dbdir = path.dirname(_dbfile)
		makedirs(dbdir, mode = 0o700, exist_ok = True)
	return _dbCheck(sqlite3.connect(_dbfile), mkdb)

def _dbCheck(db, create):
	if create:
		log.debug('create syslog db')
		db.executescript(_DB_CREATE)
		db.commit()
	return db
