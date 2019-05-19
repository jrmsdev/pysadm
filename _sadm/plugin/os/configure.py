# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys

def configure(env, data):
	env.debug(env.name())
	return {
		'platform': sys.platform,
	}
