# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from _sadm.plugin import service

def test_defaults(testing_env):
	env = testing_env(name = 'service', profile = 'plugin')
	assert env.name() == 'service'
	assert env.profile() == 'plugin'
	assert env.cfgfile() == path.join('service', 'config.ini')
	assert env.settings.sections() == []

def test_configure(testing_env):
	env = testing_env(name = 'service', profile = 'plugin')
	env.configure()
	assert sorted(env.settings.sections()) == ['sadm', 'service']
	assert env.settings.get('service', 'config.dir') == 'service'
	assert env.settings.getlist('service', 'enable') == ()

def test_enable(testing_env):
	env = testing_env(name = 'service', profile = 'plugin')
	env.configure(cfgfile = path.join('service', 'config-testing.ini'))
	assert env.settings.getlist('service', 'enable') == ('testing',)
