# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.configure import getPlugin
from _sadm.env.settings import Settings

# FIXME: fix the whole test
def test_settings():
	data = {
		'plugin0': '',
		'plugin1': [],
		'plugin2': {},
	}
	s = Settings()
	s._data = data
	assert isinstance(s._data, dict)
	assert s._data == data
	assert len(s._plugins.keys()) == 0
