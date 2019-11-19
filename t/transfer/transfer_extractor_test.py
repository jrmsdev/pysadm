# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path, unlink
from pytest import raises

from _sadm.errors import BuildError
from _sadm.transfer import extractor

def test_gen(transfer_env):
	env = transfer_env(action = 'build')
	with env.mock() as ctx:
		unlink(ctx.extractorfn)
		try:
			fn = extractor.gen(ctx.env, 'deploy')
			assert path.isfile(fn)
		finally:
			unlink(fn)
		assert path.isfile(ctx.extractorfn)
		assert path.isfile(ctx.envfn)
		assert path.isfile(ctx.zipenvfn)

# ~ def test_gen_error(transfer_env):
	# ~ env = transfer_env(action = 'build')
	# ~ with env.mock() as ctx:
		# ~ unlink(ctx.extractorfn)
		# ~ extractor.gen(ctx.env, 'deploy')
		# ~ with raises(BuildError, match = "%s file exists" % ctx.extractorfn):
			# ~ extractor.gen(ctx.env, 'deploy')
