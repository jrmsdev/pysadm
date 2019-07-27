# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from unittest.mock import Mock

class MockShUtil(object):
	_mock = None
	_cfg = None
	makedirs = None

	def __init__(self, cfg):
		self._mock = Mock()
		self.makedirs = self._mock.mock_makedirs
