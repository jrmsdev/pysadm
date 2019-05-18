# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises
from configparser import ConfigParser
from _sadm import _cfg
from _sadm.errors import Error

def test_cfg():
	assert _cfg._DEFAULT['name'] == ''
	assert _cfg._DEFAULT['profile'] == 'default'
	assert _cfg._DEFAULT['env'] == 'default'
	c = _cfg.new()
	assert isinstance(c, ConfigParser)
	assert c.name() == 'sadmtest'
	assert len(c.defaults()) == 5
	assert c.get('default', 'name') == 'sadmtest'
	assert c.get('default', 'profile') == 'testing'
	assert c.get('default', 'env') == 'testing'
	assert c.get('default', 'dir') == ''
	assert c.listPlugins('testing') == ['sadm']
	assert len(c.sections()) == 1
	assert c.has_section('testing')
	assert c.get('testing', 'dir') == './tdata'
	assert c.get('testing', 'env.testing') == 'testing/config.json'
	assert c.listProfiles() == ['testing']
	assert c.listEnvs('testing') == ['testing']

def test_profile_error():
	c = _cfg.new()
	with raises(Error, match = 'ProfileError: config profile noprofile not found'):
		c.listEnvs('noprofile')
