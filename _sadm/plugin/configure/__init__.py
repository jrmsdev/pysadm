# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

_reg = {}

def register(name):
	n = name.split('.')[-1]
	if _reg.get(n, None) is not None:
		raise RuntimeError("plugin %s already registered" % name)
	_reg[n] = name
