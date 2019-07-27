# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from unittest.mock import Mock

class MockCmd(Mock):

	def __init__(self):
		self.mock_call = self.call_manager
		self.mock_callCheck = self.callCheck_manager
