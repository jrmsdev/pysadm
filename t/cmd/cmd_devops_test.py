# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises
from unittest.mock import Mock

import _sadm.devops.devops

from _sadm.cmd import devops
from _sadm.errors import CommandError

def test_bottle(testing_cmd):
	cmd = testing_cmd(env = None)
	with cmd.mock('devops_bottle'):
		wapp = _sadm.devops.devops.wapp
		try:
			mock_bottle = Mock()
			mock_wapp = Mock()
			mock_wapp.init = Mock(return_value = mock_bottle)
			_sadm.devops.devops.wapp = mock_wapp
			devops.bottle()
			_check(mock_wapp, mock_bottle)
		finally:
			del _sadm.devops.devops.wapp
			_sadm.devops.devops.wapp = wapp

def _check(wapp, w):
	wapp.init.assert_called_with()
	wapp.config.getboolean.assert_called_with('devops', 'debug', fallback = False)
	wapp.config.getint.assert_called_with('devops', 'port', fallback = 3110)
	w.run.assert_called_once()

def _libfpath(*parts):
	fn = '/'.join(parts)
	return '/opt/src/' + fn

def test_uwsgi(testing_cmd):
	cmd = testing_cmd(env = None)
	with cmd.mock('devops_uwsgi'):
		exec_prefix = devops.sys.exec_prefix
		libfpath = devops.libdir.fpath
		try:
			devops.sys.exec_prefix = '/opt/sadm'
			devops.libdir.fpath = _libfpath
			rc = devops.uwsgi()
			assert rc == 0
		finally:
			del devops.sys.exec_prefix
			devops.sys.exec_prefix = exec_prefix
			devops.libdir.fpath = libfpath

def test_uwsgi_error(testing_cmd):
	cmd = testing_cmd(env = None)
	with cmd.mock('devops_uwsgi_error'):
		exec_prefix = devops.sys.exec_prefix
		libfpath = devops.libdir.fpath
		try:
			devops.sys.exec_prefix = '/opt/sadm'
			devops.libdir.fpath = _libfpath
			rc = devops.uwsgi()
			assert rc == 9
		finally:
			del devops.sys.exec_prefix
			devops.sys.exec_prefix = exec_prefix
			devops.libdir.fpath = libfpath
