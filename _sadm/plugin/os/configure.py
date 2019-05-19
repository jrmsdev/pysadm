# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys

def configure(env):
	env.debug(env.name())
	return {
		'platform': sys.platform,
	}
