# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from configparser import ConfigParser
from _sadm import cfg

cfg._readFiles = []

def test_cfg():
	c = cfg.new()
	assert isinstance(c, ConfigParser)
	assert len(c.defaults()) == 0
	assert len(c.sections()) == 0
