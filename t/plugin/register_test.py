# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises
from os import path

from _sadm import configure

expectPlugins = {
	0: 'sadm',
}

def test_registered_plugins():
	for n in expectPlugins.values():
		p = configure._reg.get(n, None)
		assert p is not None, "%s plugin not registered" % n
		assert p['name'] == "_sadm.plugin.%s" % n
		assert p['filename'].endswith(path.join('_sadm', 'plugin', n, '__init__.py'))

def test_pluginsList():
	idx = 0
	for p in configure.pluginsList():
		n = expectPlugins[idx]
		assert p == n, 'wrong plugin list order'

def test_plugins_order():
	order = {}
	for idx in expectPlugins.keys():
		order[idx] = expectPlugins[idx]
	assert configure._order == order, 'wrong plugin order'
