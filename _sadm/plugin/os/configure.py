# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys

def configure(env):
	sess = env.session
	sess.set('os.platform', sys.platform)
