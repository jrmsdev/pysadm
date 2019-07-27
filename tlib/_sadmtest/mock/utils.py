# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from unittest.mock import Mock

class MockCmdProc(object):
	_main = None

	def __init__(self):
		self._main = Mock()
		self.call = self._main.mock_call
		self.check_call = self._main.mock_check_call
		self._configure()

	def _configure(self):
		self.call.side_effect = [0, 0, 0, 0, 0, 0]
		self.check_call.side_effect = [0, 0]
