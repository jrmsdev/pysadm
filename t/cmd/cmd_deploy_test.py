# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises

from _sadm.cmd import deploy
from _sadm.errors import ProfileError

def test_usage_error(testing_cmd):
	cmd = testing_cmd(env = None)
	with cmd.mock('usage_error'):
		with raises(SystemExit) as err:
			deploy.main(argv = ['invalid_command'])
			assert isinstance(err, SystemExit)
			assert err.code == 2

def test_config_notfound(testing_cmd):
	cmd = testing_cmd(cfgfile = 'no-deploy.cfg', env = None)
	with cmd.mock('config_notfound'):
		with raises(ProfileError, match = 'no-deploy.cfg file not found'):
			deploy.main(argv = ['deploy'])

def test_main(testing_cmd):
	cmd = testing_cmd()
	with cmd.mock():
		rc = deploy.main(argv = ['deploy'])
		assert rc == 0
