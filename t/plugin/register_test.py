# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises
from _sadm import configure

expectPlugins = {
	0: ('sadm', '_sadm.plugin.sadm'),
}

def test_registered_plugins():
	reg = {}
	for p in expectPlugins.values():
		reg[p[0]] = p[1]
	assert configure._reg == reg, 'missing plugin'

def test_pluginsList():
	l = []
	for p in expectPlugins.values():
		l.append(p[0])
	assert [p for p in configure.pluginsList()] == l, 'missing pluginList'

def test_plugins_order():
	order = {}
	for idx in expectPlugins.keys():
		p = expectPlugins[idx]
		order[idx] = p[0]
	assert configure._order == order, 'missing plugin'
