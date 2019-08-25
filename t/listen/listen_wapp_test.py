# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import Bottle
from configparser import ConfigParser
from os import path
from pytest import raises

from _sadm.listen import wapp, errors

def test_default_config():
	assert isinstance(wapp.config, ConfigParser)
	assert wapp.config.sections() == []

def test_config_error():
	cfgfn = path.join('tdata', 'no-listen.cfg')
	with raises(FileNotFoundError):
		w = wapp.init(cfgfn = cfgfn)

ROUTES = [
	'POST /_/exec/<task>/<action>',
	'POST /hook/<provider>/<name>/<action>',
]

def test_default_wapp():
	cfgfn = path.join('tdata', 'listen.cfg')
	assert not errors._initDone
	w = wapp.init(cfgfn = cfgfn)
	assert isinstance(w, Bottle)
	assert errors._initDone
	assert sorted([p.name for p in w.plugins]) == ['json', 'sadm.listen', 'template']
	assert sorted([' '.join(str(r).split()[:2]).replace('<', '', 1).replace("'", '') for r in w.routes]) == ROUTES
