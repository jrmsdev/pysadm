# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from unittest.mock import Mock

class MockCmdProc(object):
	_mock = None
	_cfg = None
	call = None
	check_call = None

	def __init__(self):
		self._mock = Mock()
		self.call = self._mock.mock_call
		self.check_call = self._mock.mock_check_call
		self._configure()

	def _configure(self):
		self._cfg = {
			'call': 0,
			'check_call': 0,
		}
		self.call.side_effect = self._sideEffect('call')
		self.check_call.side_effect = self._sideEffect('check_call')

	def _sideEffect(self, method):
		def wrapper(*args, **kwargs):
			return self._cfg[method]
		return wrapper
