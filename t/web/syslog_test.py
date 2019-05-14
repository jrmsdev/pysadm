# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import unlink, path
from sqlite3 import Connection

from _sadm import log
from _sadm.web import syslog

_dbfile = './tdata/tmp/web/syslog.db'
syslog._dbfile = _dbfile

def _cleanup():
	if path.isfile(_dbfile):
		unlink(_dbfile)
	assert not path.isfile(_dbfile), 'could not cleanup'

def _dbInit():
	assert not path.isfile(_dbfile), 'dbfile already exists!'
	return syslog._dbInit()

_cleanup()

def test_dbInit():
	db = _dbInit()
	assert isinstance(db, Connection), 'wrong instance'
	db.close()
	assert path.isfile(_dbfile), 'db not created'
	_cleanup()

def test_initClose():
	assert isinstance(syslog._logger, syslog._webLogger), \
		'wrong instance'
	assert syslog._logger.db is None, \
		'_logger.db should be None'
	assert isinstance(log._logger, log._dummyLogger), \
		'main logger wrong instance'
	assert log._logger._child is None, \
		'main logger._child should be None'
	syslog.init()
	assert isinstance(syslog._logger.db, Connection), \
		'wrong db instance'
	assert isinstance(log._logger, log._dummyLogger), \
		'main logger wrong instance'
	assert isinstance(log._logger._child, syslog._webLogger), \
		'wrong instance'
	syslog.close()
	assert isinstance(log._logger._child, log._dummyLogger), \
		'wrong instance'
	_cleanup()
