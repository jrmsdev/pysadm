# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

_reg = {}

def register(name):
	if _reg.get(name, None) is not None:
		raise RuntimeError("plugin %s already registered" % name)
	_reg[name] = True
