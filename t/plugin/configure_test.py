# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.env.settings import Settings

def test_configure(testing_env):
	# plugins.configure is run on Env.__init__
	s = testing_env.settings
	assert isinstance(s, Settings)
