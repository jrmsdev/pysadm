# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from unittest.mock import Mock, call, mock_open

from _sadm.deploy import self_extract

_rootdir = '/opt/sadm'

@contextmanager
def mock():
	ctx = Mock()
	path = self_extract.path
	call = self_extract.call
	try:
		self_extract._vars = {
			'env': 'testing',
			'rootdir': _rootdir,
		}
		ctx.path = Mock()
		ctx.path.join.side_effect = lambda *p: '/'.join(p)
		ctx.call = Mock()
		self_extract.path = ctx.path
		self_extract.call = ctx.call
		yield ctx
	finally:
		del self_extract._vars
		self_extract._vars = {}
		del self_extract.path
		self_extract.path = path
		del self_extract.call
		self_extract.call = call

def test_main():
	with mock() as ctx:
		ctx.call.return_value = 0
		rc = self_extract.main()
		assert ctx.path.join.mock_calls == [
			call(_rootdir, 'env'),
			call(_rootdir+'/env', 'testing.env'),
			call(_rootdir, 'bin', 'sadm'),
		]
		assert ctx.call.mock_calls == [
			call('/opt/sadm/bin/sadm import /opt/sadm/env/testing.env', shell = True),
			call('/opt/sadm/bin/sadm --env testing deploy', shell = True),
		]
		assert rc == 0

def test_import_error():
	with mock() as ctx:
		ctx.call.return_value = 9
		rc = self_extract.main()
		ctx.call.assert_called_with('/opt/sadm/bin/sadm import /opt/sadm/env/testing.env',
			shell = True)
		assert rc == 9

def test_deploy_error():
	def mock_call(cmd, **kwargs):
		if cmd.endswith('--env testing deploy'):
			return 9
		return 0
	with mock() as ctx:
		ctx.call.side_effect = mock_call
		rc = self_extract.main()
		assert ctx.call.mock_calls == [
			call('/opt/sadm/bin/sadm import /opt/sadm/env/testing.env', shell = True),
			call('/opt/sadm/bin/sadm --env testing deploy', shell = True),
		]
		assert rc == 9
