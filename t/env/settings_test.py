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
