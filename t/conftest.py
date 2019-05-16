# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import pytest

from _sadm import log, _cfg
from _sadm.env import profile

log._colored = False
_cfg._readFiles = ['tdata/sadm.cfg']
profile.config = _cfg.new()

@pytest.fixture(scope = 'module')
def testing_profile(request):
	n = getattr(request.module, 'testingProfile', 'testing')
	return profile.Profile(n)
