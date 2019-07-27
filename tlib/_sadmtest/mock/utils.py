# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from unittest.mock import Mock

class MockCmdProc(object):
	_main = None

	def __init__(self):
		self._main = Mock()
		self.call = self._main.call
		self.check_call = self._main.callCheck
		self.check_call.return_valud = 128
		self.check_call.side_effect = Exception('lalala')
