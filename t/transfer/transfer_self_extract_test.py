# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from base64 import b64encode
from contextlib import contextmanager
from os import path, makedirs

from _sadm.transfer import self_extract, transfer

@contextmanager
def env_ctx(env):
	with env.mock() as ctx:
		assert self_extract._vars == {}
		assert self_extract._cargo == {}
		try:
			self_extract._vars = {
				'env': 'testing',
				'profile': 'transfer',
				'rootdir': ctx.rootdir,
			}
			self_extract._cargo = transfer.cargo(ctx.env, 'deploy')
			self_extract._artifact = ('testing.deploy', b64encode(b'testing').decode())
			yield ctx
		finally:
			del self_extract._vars
			self_extract._vars = {}
			del self_extract._cargo
			self_extract._cargo = {}

def test_extract(transfer_env):
	env = transfer_env(action = 'build')
	with env_ctx(env) as ctx:
		assert path.isfile(ctx.extractorfn)
		assert sorted(self_extract._cargo.keys()) == ['testing.env', 'testing.zip']
		dstdir = path.join(ctx.rootdir, 'env')
		assert not path.isdir(dstdir)
		self_extract.extract(dstdir)
		assert path.isdir(dstdir)
		assert path.isfile(path.join(dstdir, 'testing.env'))
		assert path.isfile(path.join(dstdir, 'testing.zip'))

def test_extract_unlink_existent(transfer_env):
	env = transfer_env(action = 'build')
	with env_ctx(env) as ctx:
		assert path.isfile(ctx.extractorfn)
		assert sorted(self_extract._cargo.keys()) == ['testing.env', 'testing.zip']
		dstdir = path.join(ctx.rootdir, 'env')
		envfn = path.join(dstdir, 'testing.env')
		zipfn = path.join(dstdir, 'testing.zip')
		makedirs(dstdir)
		for fn in (envfn, zipfn):
			with open(fn, 'x') as fh:
				fh.write('1')
		self_extract.extract(dstdir)
		assert path.isdir(dstdir)
		assert path.isfile(envfn)
		assert path.isfile(zipfn)
