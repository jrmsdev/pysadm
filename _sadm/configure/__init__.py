# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json
from os import path

try:
	from json.decoder import JSONDecodeError as jsonError
except ImportError:
	jsonError = ValueError

_reg = {}
_order = {}
_next = 0

def register(name, filename):
	global _next
	n = name.split('.')[-1]
	if _reg.get(n, None) is not None:
		raise RuntimeError("plugin %s already registered" % name)
	filename = path.abspath(path.normpath(filename))
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
	cfg = _reg[name]['config']
	env.debug(cfg)
	try:
		with open(cfg, 'r') as fh:
			return {name: json.load(fh)}
	except FileNotFoundError as err:
		raise env.error(str(err))
	except jsonError as err:
		raise env.error("config.json %s" % str(err))
