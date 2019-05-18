# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.env.settings import Settings

def test_settings():
	data = {
		'plugin0': '',
		'plugin1': [],
		'plugin2': {},
	}
	s = Settings(data)
	assert isinstance(s._data, dict)
	assert s._data == data

def test_plugins(testing_settings):
	s = testing_settings()
	assert isinstance(s, Settings)
	assert s._plugins == {'sadm': True}
	assert [p for p in s.plugins()] == ['sadm']
