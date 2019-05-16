# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.env import Env
from _sadm.env.profile import Profile

def test_env():
	e = Env('testing', 'testing', 'tdata/env/testing/config.json')
	assert isinstance(e.profile, Profile)
	assert e.name == 'testing'
	assert e.profile.name == 'testing'
	assert e.cfgfile == 'tdata/env/testing/config.json'
