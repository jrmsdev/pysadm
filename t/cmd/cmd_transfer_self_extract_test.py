# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from base64 import b64encode
from contextlib import contextmanager
from unittest.mock import Mock, call, mock_open

from _sadm.transfer import self_extract

_rootdir = '/opt/sadm'

@contextmanager
def mock():
	ctx = Mock()
	path = self_extract.path
	makedirs = self_extract.makedirs
	chmod = self_extract.chmod
	unlink = self_extract.unlink
	call = self_extract.call
	environ = self_extract.environ
	try:
		self_extract._cargo = {}
		self_extract._vars = {
			'env': 'testing',
			'profile': 'transfer',
			'rootdir': _rootdir,
		}
		self_extract._artifact = ('testing.deploy', b64encode(b'testing').decode())
		ctx.path = Mock()
		ctx.path.join.side_effect = lambda *p: '/'.join(p)
		ctx.makedirs = Mock()
		ctx.chmod = Mock()
		ctx.unlink = Mock()
		ctx.call = Mock()
		ctx.environ = {
			'SADM_ROOTDIR': '/opt/sadm',
			'SADM_PROFILE': 'transfer',
			'SADM_ENV': 'testing',
		}
		self_extract.path = ctx.path
		self_extract.makedirs = ctx.makedirs
		self_extract.chmod = ctx.chmod
		self_extract.unlink = ctx.unlink
		self_extract.call = ctx.call
		self_extract.environ = ctx.environ
		yield ctx
	finally:
		del self_extract._cargo
		self_extract._cargo = {}
		del self_extract._vars
		self_extract._vars = {}
		del self_extract._artifact
		self_extract._artifact = tuple()
		del self_extract.path
		self_extract.path = path
		del self_extract.makedirs
		self_extract.makedirs = makedirs
		del self_extract.chmod
		self_extract.chmod = chmod
		del self_extract.unlink
		self_extract.unlink = unlink
		del self_extract.call
		self_extract.call = call
		del self_extract.environ
		self_extract.environ = environ

def test_main():
	with mock() as ctx:
		ctx.call.return_value = 0
		try:
			self_extract.open = mock_open()
			rc = self_extract.main()
		finally:
			del self_extract.open
		assert ctx.path.join.mock_calls == [
			call(_rootdir, 'env'),
			call(_rootdir+'/env', 'testing.deploy'),
		]
		ctx.makedirs.assert_called_with('/opt/sadm/env', exist_ok = True)
		ctx.chmod.assert_called_with('/opt/sadm/env/testing.deploy', 0o700)
		ctx.call.assert_called_with('/opt/sadm/env/testing.deploy',
			env = ctx.environ, shell = True)
		assert rc == 0

def test_extract():
	with mock() as ctx:
		ctx.call.return_value = 9
		ctx.path.isfile.return_value = True
		self_extract._cargo.update({
			'testing.txt': 'data',
		})
		b64decode = self_extract.b64decode
		try:
			self_extract.open = mock_open()
			self_extract.b64decode = Mock()
			self_extract.b64decode.return_value = 'testing'
			rc = self_extract.main()
		finally:
			assert self_extract.open.mock_calls == [
				call('/'.join((_rootdir, 'env', 'testing.txt')), 'wb'),
				call().__enter__(),
				call().write('testing'),
				call().__exit__(None, None, None),
				call('/'.join((_rootdir, 'env', 'testing.deploy')), 'wb'),
				call().__enter__(),
				call().write('testing'),
				call().__exit__(None, None, None),
			]
			assert self_extract.b64decode.mock_calls == [
				call(b'data'),
				call(b'dGVzdGluZw=='),
			]
			fh = self_extract.open()
			# ~ fh.write.assert_called_once_with('testing')
			assert fh.write.mock_calls == [call('testing'), call('testing')]
			del self_extract.open
			self_extract.b64decode = b64decode
		ctx.call.assert_called_with('/opt/sadm/env/testing.deploy',
			env = ctx.environ, shell = True)
		assert rc == 9
