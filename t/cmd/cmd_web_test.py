# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from unittest.mock import Mock

import _sadm.web

from _sadm.cmd import web

def test_main(testing_cmd):
	cmd = testing_cmd(env = None)
	with cmd.mock('web_main'):
		wapp = _sadm.web.wapp
		try:
			mock_wapp = Mock()
			_sadm.web.wapp = mock_wapp
			web.main(argv = [])
			mock_wapp.run.assert_called_with(debug = False, host = 'localhost',
				port = 3478, quiet = True, reloader = False)
		finally:
			del _sadm.web.wapp
			_sadm.web.wapp = wapp

def test_debug(testing_cmd):
	cmd = testing_cmd(env = None)
	with cmd.mock('web_debug'):
		wapp = _sadm.web.wapp
		try:
			mock_wapp = Mock()
			_sadm.web.wapp = mock_wapp
			web.main(argv = ['--debug'])
			mock_wapp.run.assert_called_with(debug = True, host = 'localhost',
				port = 3478, quiet = False, reloader = True)
		finally:
			del _sadm.web.wapp
			_sadm.web.wapp = wapp
