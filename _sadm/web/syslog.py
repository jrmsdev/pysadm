# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys
import sqlite3
from os import path, makedirs

from _sadm import log

class _webLogger(object):

	def __init__(self, db):
		self.db = db

	def close(self):
		self.db.close()

	def error(self, msg):
		print("[SYSLOG] E:", msg, file = sys.stderr)

	def warn(self, msg):
		print("[SYSLOG] W:", msg, file = sys.stderr)

	def info(self, msg):
		print("[SYSLOG] I:", msg, file = sys.stdout)

	def msg(self, msg):
		print("[SYSLOG]", msg, file = sys.stdout)

def init():
	log.debug('init web syslog')
	try:
		db = _dbInit()
	except Exception as e:
		log.error("could not init web syslog: %s" % e)
	else:
		log.debug('attach child logger')
		log._logger._child = _webLogger(db)
		log.info('syslog start')

def close():
	log.info('syslog end')
	log._logger.close()

_dbfile = path.expanduser('~/.local/sadm/syslog.db')

def _dbInit():
	log.debug("syslog init %s" % _dbfile)
	log.debug("sqlite version %s (lib %s)" % (sqlite3.version, sqlite3.sqlite_version))
	dbdir = path.dirname(_dbfile)
	makedirs(dbdir, mode = 0o700, exist_ok = True)
	return sqlite3.connect(_dbfile)
