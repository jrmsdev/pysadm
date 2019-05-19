# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.configure import getPlugin
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
	assert len(s._plugins.keys()) == 3
	assert s._plugins == {'plugin0': True, 'plugin1': True, 'plugin2': True,}
