# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises
from os import path

from _sadm import configure

expectPlugins = {
	0: 'sadm',
	1: 'os',
	2: 'testing',
}

def test_registered_plugins():
	for n in expectPlugins.values():
		p = configure._reg.get(n, None)
		assert p is not None, "%s plugin not registered" % n
		assert p['name'] == "_sadm.plugin.%s" % n
		assert p['config'].endswith(path.join('_sadm', 'plugin', n, 'config.json'))

def test_pluginsList():
	idx = 0
	for p in configure.pluginsList():
		n = expectPlugins[idx]
		assert p == n, 'wrong plugin list order'
		idx += 1

def test_plugins_order():
	assert configure._order == expectPlugins, 'wrong plugins order'
