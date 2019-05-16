# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import pytest

from _sadm import log
log._colored = False

from _sadm import _cfg
_cfg._cfgFile = './tdata/sadm.cfg'

import _sadm
del _sadm.config
_sadm.config = _cfg.new()

from _sadm import env
from _sadm.env import profile

@pytest.fixture(scope = 'module')
def testing_profile(request):
	n = getattr(request.module, 'testingProfile', 'testing')
	return profile.Profile(n)

@pytest.fixture(scope = 'module')
def testing_env(request):
	p = getattr(request.module, 'testingProfile', 'testing')
	n = getattr(request.module, 'testingEnv', 'testing')
	return env.Env(p, n)
