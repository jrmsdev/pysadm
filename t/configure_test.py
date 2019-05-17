# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.env.settings import Settings
from _sadm.configure import plugins

def test_configure(testing_env):
	env = testing_env
	s = plugins.configure(env, env._cfgfile)
	assert isinstance(s, Settings)
