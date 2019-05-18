# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.env import Env
from _sadm.env.settings import Settings
from _sadm.configure import plugins, pluginInit

def test_configure():
	env = Env('testing', 'testing')
	s = plugins.configure(env, env._cfgfile)
	assert isinstance(s, Settings)

def test_pluginInit(testing_env):
	env = testing_env
	pluginInit(env, 'sadm')
