# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from unittest.mock import Mock

class MockCmdProc(object):
	_mock = None
	_cfg = None
	call = None
	check_call = None

	def __init__(self, cfg):
		self._mock = Mock()
		self.call = self._mock.mock_call
		self.check_call = self._mock.mock_check_call
		self._configure(cfg)

	def _configure(self, cfg):
		self._cfg = self._parseConfig(cfg)
		self.call.side_effect = self._sideEffect('call')
		self.check_call.side_effect = self._sideEffect('check_call')

	def _parseConfig(self, cfg):
		d = {}
		if cfg is None:
			return d
		d['call'] = self._parseCmdOptions(cfg, 'cmd.call')
		d['check_call'] = self._parseCmdOptions(cfg, 'cmd.check_call')
		return d

	def _parseCmdOptions(self, cfg, opt):
		d = {}
		data = cfg.get(opt, fallback = '')
		if data != '':
			for line in data.splitlines():
				line = line.strip()
				if line == '':
					continue
				elif line.startswith('#'):
					continue
				i = line.split(';')
				retval = int(i[0])
				cmdline = ';'.join(i[1:]).strip()
				d[cmdline] = retval
		return d

	def _sideEffect(self, method):
		def wrapper(args, **kwargs):
			if not method in self._cfg:
				raise KeyError("%s method is not configured (yet)" % method)
			if isinstance(args, list):
				cmdline = ' '.join(args)
			else:
				cmdline = args
			try:
				return self._cfg[method][cmdline]
			except KeyError as err:
				raise KeyError("%s - %s method" % (str(err), method))
		return wrapper
