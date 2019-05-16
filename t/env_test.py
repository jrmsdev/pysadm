# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises
from _sadm.errors import Error
from _sadm.env import Env
from _sadm.env.profile import Profile

def test_env(testing_env):
	e = testing_env
	assert isinstance(e, Env)
	assert e.name == 'testing'
	assert e.cfgfile == 'testing/config.json'
	assert isinstance(e.profile, Profile)

def test_env_error(testing_env):
	e = testing_env
	e.name = 'noenv'
	with raises(Error, match = 'EnvError: noenv env not found'):
		e._load()
