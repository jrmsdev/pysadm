# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from unittest.mock import Mock

import _sadm.listen

from _sadm.cmd import listen

def test_bottle(testing_cmd):
	cmd = testing_cmd(env = None)
	with cmd.mock('listen_bottle'):
		wapp = _sadm.listen.wapp
		try:
			mock_bottle = Mock()
			mock_wapp = Mock()
			mock_wapp.init = Mock(return_value = mock_bottle)
			_sadm.listen.wapp = mock_wapp
			listen.bottle()
			_check(mock_wapp, mock_bottle)
		finally:
			del _sadm.listen.wapp
			_sadm.listen.wapp = wapp

def _check(wapp, w):
	wapp.init.assert_called_with()
	wapp.config.getboolean.assert_called_with('sadm.listen', 'debug', fallback = False)
	wapp.config.get.assert_called_with('sadm.listen', 'host', fallback = '127.0.0.1')
	wapp.config.getint.assert_called_with('sadm.listen', 'port', fallback = 3666)
	w.run.assert_called()
