# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises

from _sadm.cmd import deploy
from _sadm.errors import ProfileError

def test_usage_error(testing_cmd):
	with testing_cmd() as ctx:
		with raises(SystemExit) as err:
			deploy.main(argv = ['invalid_command'])
			assert isinstance(err, SystemExit)
			assert err.code == 2

def test_config_notfound(testing_cmd):
	with testing_cmd() as ctx:
		with raises(ProfileError, match = 'deploy.cfg file not found'):
			deploy.main(argv = ['deploy'])

# ~ def test_main(testing_cmd):
	# ~ with testing_cmd() as ctx:
		# ~ deploy.main(argv = ['deploy'])
