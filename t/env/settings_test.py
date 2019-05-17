# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.env import Settings

def test_settings(testing_settings):
	s = testing_settings
	assert isinstance(s, Settings)
	assert s._profile == 'testing'
	assert s._env == 'testing'
	assert s._filename == 'testing/config.json'
