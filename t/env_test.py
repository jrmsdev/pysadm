# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises

from _sadm import asset
from _sadm.env import Env
from _sadm.env.profile import Profile
from _sadm.env.settings import Settings
from _sadm.errors import EnvError

def test_env(testing_env):
	e = testing_env
	assert isinstance(e, Env)
	assert e._cfgfile == 'config.json'
	assert e.name() == 'testing'
	assert isinstance(e._profile, Profile)
	assert e._profile.name() == 'testing'
	assert isinstance(e.assets, asset.Manager)
	e.configure()
	assert isinstance(e.settings, Settings)

def test_env_error(testing_env):
	with raises(EnvError, match = 'env not found'):
		Env('testing', 'noenv')
	e = testing_env
	e._cfgfile = ''
	with raises(EnvError, match = 'config file not set'):
		e._loadcfg()
