# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import pytest

# logger

from _sadm import log
log._colored = False

# register testing plugin

import _sadm.plugin.testing

# config

from _sadm import _cfg
_cfg._cfgFile = './tdata/sadm.cfg'

# attach testing config

import _sadm
del _sadm.config
_sadm.config = _cfg.new()

# testing profile

from _sadm.env import profile

@pytest.fixture(scope = 'module')
def testing_profile(request):
	n = getattr(request.module, 'testingProfile', 'testing')
	return profile.Profile(n)

# testing env

from _sadm import env

@pytest.fixture(scope = 'module')
def testing_env(request):
	def wrapper(name = 'testing', profile = 'testing'):
		return env.Env(profile, name)
	return wrapper
