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
			'call': {
				'/usr/bin/dpkg-query -s less >/dev/null 2>/dev/null': 0,
				'/usr/bin/dpkg-query -s vim-tiny >/dev/null 2>/dev/null': 0,
				'/usr/bin/dpkg-query -s sudo >/dev/null 2>/dev/null': 0,
				'/usr/bin/dpkg-query -s rsync >/dev/null 2>/dev/null': 0,
				'/usr/bin/dpkg-query -s python3 >/dev/null 2>/dev/null': 0,
				'/usr/bin/dpkg-query -s nano >/dev/null 2>/dev/null': 0,
			},
			'check_call': {
				'apt-get update': 0,
				'apt-get autoremove -yy --purge nano': 0,
			}
		}
		self.call.side_effect = self._sideEffect('call')
		self.check_call.side_effect = self._sideEffect('check_call')

	def _sideEffect(self, method):
		def wrapper(args, **kwargs):
			if isinstance(args, list):
				cmdline = ' '.join(args)
			else:
				cmdline = args
			return self._cfg[method][cmdline]
		return wrapper
