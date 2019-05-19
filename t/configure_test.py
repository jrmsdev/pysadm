# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises
from os import path

from _sadm.configure import plugins, pluginInit, register, jsonError, getPlugin
from _sadm.env import Env
from _sadm.env.settings import Settings
from _sadm.errors import EnvError, PluginError

def test_configure():
	env = Env('testing', 'testing')
	s = plugins.configure(env, env._cfgfile)
	assert isinstance(s, Settings)

def test_pluginInit(testing_env):
	env = testing_env()
	data = pluginInit(env, 'sadm')
	assert isinstance(data, dict)
	assert [p for p in data.keys()] == ['sadm']
	with raises(EnvError, match = 'config.nofile file not found'):
		pluginInit(env, 'sadm', cfg = 'config.nofile')
	cfg = path.join('tdata', 'testing', 'config-invalid.json')
	with raises(EnvError, match = "%s Expecting value:" % cfg):
		pluginInit(env, 'sadm', cfg = cfg)

def test_getcfg(testing_env):
	env = testing_env()
	cfg = plugins._getcfg(env, 'config.json')
	assert isinstance(cfg, dict)
	with raises(EnvError, match = 'invalid config name \'fake\''):
		plugins._getcfg(env, 'config-name-error.json')

def test_load(testing_env):
	env = testing_env()
	cfg = plugins._getcfg(env, 'config.json')
	assert isinstance(cfg, dict)
	data = plugins._load(env, cfg, enabledPlugins = {'sadm': True})
	assert isinstance(data, dict)
	assert [p for p in data.keys()] == ['sadm']

def test_default_plugins(testing_env):
	env = testing_env()
	cfg = plugins._getcfg(env, 'config.json')
	data = plugins._load(env, cfg)
	assert [p for p in data.keys()] == ['sadm', 'os', 'testing']

def test_disabled_plugin(testing_env):
	env = testing_env()
	cfg = plugins._getcfg(env, 'config.json')
	data = plugins._load(env, cfg, enabledPlugins = {})
	assert data == {}

def test_plugin_data(testing_env):
	env = testing_env()
	cfg = plugins._getcfg(env, 'config-plugin-data.json')
	data = plugins._load(env, cfg)
	assert [p for p in data.keys()] == ['sadm', 'os', 'testing']
	# ~ assert data['testing'] == 'testing_data'

def test_register_error():
	with raises(RuntimeError, match = 'plugin sadm already registered'):
		register('sadm', 'filename')

def test_getPluginError():
	with raises(PluginError, match = 'noname plugin not found'):
		getPlugin('noname', 'configure')
	with raises(PluginError, match = 'testing plugin nomod not implemented'):
		getPlugin('testing', 'nomod')

def test_getPlugin():
	mod = getPlugin('testing', 'configure')
	assert str(mod).startswith('<module \'_sadm.plugin.testing.configure\' from')
