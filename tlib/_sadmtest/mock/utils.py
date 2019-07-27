# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from unittest.mock import Mock

class MockCmd(object):
	_main = None

	def __init__(self):
		self._main = Mock()
		self.mock_call = self._main.call
		self.mock_callCheck = self._main.callCheck
