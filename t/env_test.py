# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.env import Env
from _sadm.env.profile import Profile

def test_env(testing_env):
	e = testing_env
	assert isinstance(e, Env)
	assert e.name == 'testing'
	assert e.cfgfile == 'testing/config.json'
	assert isinstance(e.profile, Profile)
