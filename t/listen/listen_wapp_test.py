# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json

from configparser import ConfigParser
from glob import glob
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
]

def test_default_wapp():
	cfgfn = path.join('tdata', 'listen.cfg')
	assert not errors._initDone
	w = wapp.init(cfgfn = cfgfn)
	assert errors._initDone
	assert sorted([p.name for p in w.plugins]) == ['sadm.listen.response']
	routes = []
	for r in w.routes:
		routes.append(' '.join([str(r.name), r.rule, r.method]))
	assert sorted(routes) == ROUTES

def test_wapp(listen_wapp):
	with listen_wapp() as w:
		assert w.name == 'listen'
		assert w.response is None

WEBHOOK_ROUTES = ROUTES[:]
WEBHOOK_ROUTES.extend([
	'hook.repo /hook/<provider>/<name>/<action> POST',
])

def test_webhook_routes(listen_wapp):
	with listen_wapp(profile = 'testing') as w:
		assert w.name == 'listen'
		assert w.response is None
		routes = []
		for r in w.routes:
			routes.append(' '.join([str(r.name), r.rule, r.method]))
		assert sorted(routes) == WEBHOOK_ROUTES

def test_all(listen_wapp):
	patterns = [
		path.join('tdata', 'listen', '*', 'listen.cfg'),
	]
	cfgfiles = {}
	for patt in patterns:
		for fn in glob(patt):
			cfgfiles[fn] = True
	for fn in sorted(cfgfiles.keys()):
		profile = fn.replace(path.join('tdata', 'listen'), '', 1)
		profile = '/'.join(profile.split(path.sep)[:-1])
		if profile.startswith('/'):
			profile = profile[1:]
			_testProfile(listen_wapp, profile, fn)

def _testProfile(listen_wapp, profile, cfgfn):
	print(profile, cfgfn)
	profdir = path.dirname(cfgfn)
	for datfn in sorted(glob(path.join(profdir, '*.json'))):
		datname = path.basename(datfn).replace('.json', '')
		print(' ', datname, datfn)
		with open(datfn, 'r') as fh:
			dat = json.load(fh)
		hndlr = dat['handler']['name']
		hargs = dat['handler'].get('args', [])
		hmeth = dat['handler'].get('method', 'GET')
		if dat.get('data', None) is not None:
			hmeth = 'POST'
		with listen_wapp(profile = profile) as wapp:
			hfunc = _getHandler(wapp, hndlr)
			if hmeth == 'POST':
				_wappPOST(wapp, datname, hfunc, hargs)
			_wappCheck(wapp, dat.get('response', 'OK'))

def _getHandler(wapp, name):
	for r in wapp.routes:
		if r.name == name:
			return r.callback
	print('wapp routes', wapp.routes)
	assert False, "wapp handler not found: %s" % name

def _wappPOST(wapp, datname, hfunc, hargs):
	wapp.POST(datname, hfunc, *hargs)

def _wappCheck(wapp, resp):
	assert wapp.response == resp
