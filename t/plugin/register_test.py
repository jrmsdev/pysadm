# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises
from _sadm import configure

expectPlugins = {
	'sadm': '_sadm.plugin.sadm',
}

def test_registered_plugins():
	assert configure._reg == expectPlugins, 'missing plugin'

def test_reg():
	configure.register(__name__)
	assert configure._reg['register_test'] == 'register_test'
	assert configure._reg.get('register_test', None) is not None
	with raises(RuntimeError):
		configure.register(__name__)
	del configure._reg['register_test']
	assert configure._reg.get('register_test', None) is None

def test_pluginsList():
	assert [p for p in configure.pluginsList()] == [n for n in expectPlugins.keys()], \
		'missing pluginList'
