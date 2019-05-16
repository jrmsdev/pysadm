# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from configparser import ConfigParser
from _sadm import _cfg as cfg

def test_cfg():
	c = cfg.new()
	assert isinstance(c, ConfigParser)
	assert len(c.defaults()) == 2
	assert len(c.sections()) == 1
	assert c.has_section('testing')
	assert c.get('testing', 'dir') == './tdata'
	assert c.get('testing', 'env.testing') == 'testing/config.json'
	assert c.listProfiles() == ['testing']
	assert c.listEnvs('testing') == ['testing']
