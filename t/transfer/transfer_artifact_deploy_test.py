# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path, unlink
from pytest import raises

from _sadm.errors import BuildError
from _sadm.transfer import extractor

def test_env_error(transfer_env):
	env = transfer_env(action = 'build')
	with env.mock() as ctx:
		assert path.isfile(ctx.extractorfn)
		assert path.isfile(ctx.envfn)
		unlink(ctx.extractorfn)
		unlink(ctx.envfn)
		with raises(BuildError, match = "%s file not found" % ctx.envfn):
			extractor.gen(ctx.env, 'deploy')

def test_zipenv_error(transfer_env):
	env = transfer_env(action = 'build')
	with env.mock() as ctx:
		assert path.isfile(ctx.extractorfn)
		assert path.isfile(ctx.zipenvfn)
		unlink(ctx.extractorfn)
		unlink(ctx.zipenvfn)
		with raises(BuildError, match = "%s file not found" % ctx.zipenvfn):
			extractor.gen(ctx.env, 'deploy')
