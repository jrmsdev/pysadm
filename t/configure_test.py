# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.env import Env
from _sadm.env.settings import Settings
from _sadm.configure import plugins

def test_configure():
	env = Env('testing', 'testing')
	s = plugins.configure(env, env._cfgfile)
	assert isinstance(s, Settings)
