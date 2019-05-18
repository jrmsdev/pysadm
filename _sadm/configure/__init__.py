# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

_reg = {}
_order = {}
_next = 0

def register(name, filename):
	global _next
	n = name.split('.')[-1]
	if _reg.get(n, None) is not None:
		raise RuntimeError("plugin %s already registered" % name)
	_reg[n] = {
		'name': name,
		'config': path.join(path.dirname(filename), 'config.json'),
	}
	_order[_next] = n
	_next += 1

def pluginsList():
	for idx in sorted(_order.keys()):
		yield _order[idx]

def pluginInit(env, name):
	env.debug("plugin %s" % name)
