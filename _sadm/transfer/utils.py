# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from base64 import b64encode

__all__ = ['load']

def load(env, filename):
	env.debug("load %s" % filename)
	with open(filename, 'rb') as fh:
		return b64encode(fh.read()).decode()
