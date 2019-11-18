# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from _sadm.transfer import utils

def test_load(transfer_env):
	env = transfer_env(action = 'build')
	with env.mock() as ctx:
		tmpfn = path.join(ctx.tmpdir, 'testing.txt')
		assert not path.isfile(tmpfn)
		with open(tmpfn, 'x') as fh:
			fh.write('testing')
		enc = utils.load(ctx.env, tmpfn)
		assert enc == 'dGVzdGluZw=='
