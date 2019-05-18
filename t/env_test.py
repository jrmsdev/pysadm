# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises
from time import time

from _sadm import asset
from _sadm.env import Env
from _sadm.env.profile import Profile
from _sadm.env.settings import Settings
from _sadm.errors import EnvError

def test_env(testing_env):
	e = testing_env
	assert isinstance(e, Env)
	assert e._cfgfile == 'config.json'
	assert e.name() == 'testing'
	assert isinstance(e._profile, Profile)
	assert e._profile.name() == 'testing'
	assert isinstance(e.assets, asset.Manager)
	e.configure()
	assert isinstance(e.settings, Settings)

def test_env_error(testing_env):
	with raises(EnvError, match = 'env not found'):
		Env('testing', 'noenv')
	e = testing_env
	e._cfgfile = ''
	with raises(EnvError, match = 'config file not set'):
		e._loadcfg()

def test_load_error(testing_env):
	e = testing_env
	with raises(EnvError, match = 'config file not set'):
		e._load(fn = '')
	with raises(EnvError, match = 'testing profile dir not set'):
		e._load(pdir = '')

def test_start_end_action(testing_env):
	e = testing_env
	e._run = {}
	assert [n for n in e._run.keys()] == []
	e.start('testing_action')
	assert [n for n in e._run.keys()] == ['testing_action']
	assert e._run['testing_action'].get('start', '') != ''
	assert e._run['testing_action'].get('tag.prev', None) is not None
	assert e._run['testing_action'].get('end', None) is None
	e.end('testing_action')
	assert e._run['testing_action'].get('end', '') != ''

def test_start_end_error(testing_env):
	e = testing_env
	e._run = {}
	assert [n for n in e._run.keys()] == []
	e.start('testing_error')
	with raises(EnvError, match = 'testing_error action already started'):
		e.start('testing_error')
	assert [n for n in e._run.keys()] == ['testing_error']
	with raises(EnvError, match = 'testing_end_error action was not started'):
		e.end('testing_end_error')

def test_report(testing_env):
	e = testing_env
	e._run = {}
	e.start('action1')
	e.end('action1')
	e.report('testing_report')
	e.report('testing_report', startTime = time() - 10)
	e.start('action2')
	with raises(EnvError, match = 'not finished action\(s\): action2'):
		e.report('testing_report')
