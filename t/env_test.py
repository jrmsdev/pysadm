# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises
from _sadm.errors import EnvError
from _sadm.env import Env
from _sadm.env.profile import Profile

def test_env(testing_env):
	e = testing_env
	assert isinstance(e, Env)
	assert e._cfgfile == 'testing/config.json'
	assert e.name() == 'testing'
	assert isinstance(e._profile, Profile)
	assert e._profile.name() == 'testing'

def test_env_error(testing_env):
	e = testing_env
	e._name = 'noenv'
	with raises(EnvError, match = 'env not found'):
		e._load()
	e._name = 'testing'
	e._cfgfile = ''
	with raises(EnvError, match = 'config file not set'):
		e._loadcfg()
