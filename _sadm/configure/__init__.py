# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

_reg = {}
_order = {}
_next = 0

def register(name):
	global _next
	n = name.split('.')[-1]
	if _reg.get(n, None) is not None:
		raise RuntimeError("plugin %s already registered" % name)
	_reg[n] = name
	_order[_next] = n
	_next += 1

def pluginsList():
	for idx in sorted(_order.keys()):
		yield _order[idx]
