# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import pytest
from os import path, makedirs, unlink
from shutil import rmtree

# logger

from _sadm import log
log._colored = False
log.init('quiet')

# register testing plugin

import _sadm.plugin.testing

# config

from _sadm import cfg
cfg._cfgFile = path.join('tdata', 'sadm.cfg')

# attach testing config

import _sadm
del _sadm.config
_sadm.config = cfg.new()

# configure plugins testing

from _sadm.plugin.utils import builddir
builddir._builddir = path.join('tdata', 'builddir')
makedirs(path.join(builddir._builddir, 'testing', 'testing'), exist_ok = True)

# testing profile

from _sadm.env import profile

@pytest.fixture
def testing_profile():
	def wrapper(name = 'testing'):
		return profile.Profile(name)
	return wrapper

# testing env

from _sadm import env

@pytest.fixture
def testing_env():
	def wrapper(name = 'testing', profile = 'testing'):
		e = env.Env(profile, name)
		_cleanEnv(e)
		return e
	return wrapper

# testing settings

@pytest.fixture
def testing_settings():
	envmod = env
	def wrapper(profile = 'testing', env = 'testing', cfgfile = None):
		if cfgfile is not None:
			cfgfile = path.join(profile, cfgfile)
		e = envmod.Env(profile, env)
		_cleanEnv(e)
		e.configure(cfgfile = cfgfile)
		return e.settings
	return wrapper

# testing env setup

from _sadm.env import cmd as envcmd

@pytest.fixture
def env_setup():
	def wrapper(name = 'testing', profile = 'envsetup',
		configure = False, cfgfile = None, action = None):
		if action is not None:
			configure = False # configure in called from cmd.run
		e = env.Env(profile, name)
		_cleanEnv(e)
		if configure:
			e.configure(cfgfile = cfgfile)
		if action is not None:
			envcmd.run(e, action)
		return e
	return wrapper

def _cleanEnv(env):
	en = env.name()
	bdir = path.realpath(path.join('tdata', 'builddir', env.profile()))
	pdir = path.realpath(path.join('tdata', env.profile()))
	_bdirs = [
		path.join(bdir, en),
		path.join(bdir, en + '.meta'),
	]
	for d in _bdirs:
		if path.isdir(d):
			rmtree(d)
	_bfiles = [
		path.join(bdir, en + '.lock'),
		path.join(bdir, en + '.zip'),
		path.join(bdir, en + '.checksum'),
		path.join(pdir, en, '.lock'),
	]
	for f in _bfiles:
		if path.isfile(f):
			unlink(f)
