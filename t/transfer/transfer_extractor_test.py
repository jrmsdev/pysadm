# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path, unlink
from pytest import raises

from _sadm.transfer import extractor
from _sadm.errors import BuildError

def test_gen(transfer_env):
	env = transfer_env(action = 'build')
	with env.mock() as ctx:
		unlink(ctx.extractorfn)
		extractor.gen(ctx.env, 'deploy')
		assert path.isfile(ctx.extractorfn)
		assert path.isfile(ctx.envfn)
		assert path.isfile(ctx.zipenvfn)

def test_gen_error(transfer_env):
	env = transfer_env(action = 'build')
	with env.mock() as ctx:
		unlink(ctx.extractorfn)
		extractor.gen(ctx.env, 'deploy')
		with raises(BuildError, match = "%s file exists" % ctx.extractorfn):
			extractor.gen(ctx.env, 'deploy')

# ~ def test_env_error(env_setup):
	# ~ env = env_setup(action = 'build')
	# ~ assert path.isfile(extractorfn)
	# ~ assert path.isfile(envfn)
	# ~ unlink(extractorfn)
	# ~ unlink(envfn)
	# ~ with raises(BuildError, match = "%s file not found" % envfn):
		# ~ extractor.gen(env)

# ~ def test_zipenv_error(env_setup):
	# ~ env = env_setup(action = 'build')
	# ~ assert path.isfile(extractorfn)
	# ~ assert path.isfile(zipenvfn)
	# ~ unlink(extractorfn)
	# ~ unlink(zipenvfn)
	# ~ with raises(BuildError, match = "%s file not found" % zipenvfn):
		# ~ extractor.gen(env)
