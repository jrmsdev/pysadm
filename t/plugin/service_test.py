# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from _sadm.plugin import service

def test_defaults(testing_env):
	env = testing_env('plugin.service')
	assert env.name() == 'plugin.service'
	assert env.profile() == 'testing'
	assert env.cfgfile() == path.join('plugin', 'service.ini')
	assert env.settings.sections() == []

def test_configure(testing_env):
	env = testing_env('plugin.service')
	env.configure()
	assert sorted(env.settings.sections()) == ['os', 'sadm', 'service', 'testing']
