# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises

from _sadm.errors import BuildError
from _sadm.transfer import transfer

def test_cargo_error(transfer_env):
	env = transfer_env()
	with env.mock() as ctx:
		with raises(BuildError, match = 'unknown artifact: invalid.artifact'):
			transfer.cargo(ctx.env, 'invalid.artifact')
