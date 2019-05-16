# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from configparser import ConfigParser
from _sadm import _cfg

def test_cfg():
	assert _cfg._DEFAULT['name'] == ''
	assert _cfg._DEFAULT['profile'] == 'default'
	assert _cfg._DEFAULT['env'] == 'default'
	c = _cfg.new()
	assert isinstance(c, ConfigParser)
	assert c.name() == 'sadmtest'
	assert len(c.defaults()) == 3
	assert c.get('default', 'name') == 'sadmtest'
	assert c.get('default', 'profile') == 'default'
	assert c.get('default', 'env') == 'default'
	assert len(c.sections()) == 1
	assert c.has_section('testing')
	assert c.get('testing', 'dir') == './tdata'
	assert c.get('testing', 'env.testing') == 'testing/config.json'
	assert c.listProfiles() == ['testing']
	assert c.listEnvs('testing') == ['testing']
