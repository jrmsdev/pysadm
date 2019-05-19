# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys

def configure(env, cfg):
	env.debug(env.name())
	s = env.settings2
	s.set('os', 'platform', sys.platform)
