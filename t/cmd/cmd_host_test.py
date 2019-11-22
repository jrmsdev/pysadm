# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.cmd import host

def test_main(testing_cmd):
	cmd = testing_cmd(env = None)
	with cmd.mock('host_main'):
		rc = host.main(['--exec', 'testing/exec.sh'])
		assert rc == 0

def test_no_action(testing_cmd):
	cmd = testing_cmd(env = None)
	with cmd.mock('no_action'):
		rc = host.main([])
		assert rc == 19

def test_env_error(testing_cmd):
	cmd = testing_cmd(env = None)
	with cmd.mock('env_error'):
		rc = host.main(['--env', 'invalid.env'])
		assert rc == 9
