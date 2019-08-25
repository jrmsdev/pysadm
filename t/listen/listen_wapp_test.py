# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from configparser import ConfigParser
from os import path
from pytest import raises

from _sadm.listen import wapp, errors

def test_default_config():
	assert wapp.config is None

def test_config_error():
	cfgfn = path.join('tdata', 'no-listen.cfg')
	with raises(FileNotFoundError):
		w = wapp.init(cfgfn = cfgfn)

ROUTES = [
	'_exec /_/exec/<task>/<action> POST',
	'hook.repo /hook/<provider>/<name>/<action> POST',
]

def test_default_wapp():
	cfgfn = path.join('tdata', 'listen.cfg')
	assert errors._initDone
	w = wapp.init(cfgfn = cfgfn)
	assert sorted([p.name for p in w.plugins]) == ['sadm.listen']
	routes = []
	for r in w.routes:
		routes.append(' '.join([str(r.name), r.rule, r.method]))
	assert sorted(routes) == ROUTES

def test_wapp(listen_wapp):
	with listen_wapp() as w:
		assert w.name == 'listen'
		assert w.response is None
