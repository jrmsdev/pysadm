# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import pytest

from _sadm import log, _cfg, env
from _sadm.env import profile

log._colored = False

_cfg._cfgFile = 'tdata/sadm.cfg'
config = _cfg.new()

profile.config = config
env.config = config

@pytest.fixture(scope = 'module')
def testing_profile(request):
	n = getattr(request.module, 'testingProfile', 'testing')
	return profile.Profile(n)

@pytest.fixture(scope = 'module')
def testing_env(request):
	p = getattr(request.module, 'testingProfile', 'testing')
	n = getattr(request.module, 'testingEnv', 'testing')
	return env.Env(p, n)
