# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.env.settings import Settings

def test_settings(testing_settings):
	s = testing_settings
	assert isinstance(s, Settings)
	assert isinstance(s._data, dict)
