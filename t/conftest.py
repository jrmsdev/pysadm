# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import pytest

import _sadm
import _sadm.log
import _sadm._cfg

_sadm.log._colored = False
_sadm._cfg._cfgFile = './tdata/sadm.cfg'
del _sadm.config
_sadm.config = _sadm._cfg.new()

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
