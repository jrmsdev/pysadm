# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
import sqlite3
from os import path, makedirs

from _sadm import log

# SQL stuff

_DB_CREATE = """
create table syslog (
	id integer primary key autoincrement,
	time text default current_timestamp,
	level integer,
	msg text
);
"""
_LVLMAP = {
	'error': 3,
	'warn': 2,
	'info': 1,
	'msg': 0,
}
_LOG_INSERT = 'insert into syslog (level, msg) values (?, ?)'

# underlying logger class

class _webLogger(object):
	db = None

	def error(self, msg):
		self.db.execute(_LOG_INSERT, (_LVLMAP['error'], msg))
		self.db.commit()
		print("[syslog] E:", msg, file = sys.stderr)

	def warn(self, msg):
		self.db.execute(_LOG_INSERT, (_LVLMAP['warn'], msg))
		self.db.commit()
		print("[syslog] W:", msg, file = sys.stderr)

	def info(self, msg):
		self.db.execute(_LOG_INSERT, (_LVLMAP['info'], msg))
		self.db.commit()
		print("[syslog] I:", msg, file = sys.stdout)

	def msg(self, msg):
		self.db.execute(_LOG_INSERT, (_LVLMAP['msg'], msg))
		self.db.commit()
		print("[syslog]", msg, file = sys.stdout)

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

# default logger

_logger = _webLogger()
_dbfile = path.expanduser('~/.local/sadm/syslog.db')

# public methods

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
		_logger.db.close()
		log._logger._child = log._dummyLogger()
