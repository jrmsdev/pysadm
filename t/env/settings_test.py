# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.env.settings import Settings

def test_settings():
	data = {
		'plugin0': '',
		'plugin1': [],
		'plugin2': {},
	}
	cfg = {
		'plugin0': 'v0',
	}
	rst = {}
	rst.update(data)
	rst.update(cfg)
	s = Settings(data, cfg)
	assert isinstance(s._data, dict)
	assert s._data == rst
