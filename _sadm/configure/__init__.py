# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json
from os import path

try:
	# python >=3.5
	from json.decoder import JSONDecodeError as jsonError
except ImportError: # pragma: no cover
	# python 3.4
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

def pluginInit(env, name, cfg = None):
	env.debug("plugin %s" % name)
	if cfg is None:
		cfg = _reg[name]['config']
	env.debug(cfg)
	try:
		with open(cfg, 'r') as fh:
			return {name: json.load(fh)}
	except FileNotFoundError as err:
		raise env.error("%s file not found" % cfg)
	except jsonError as err:
		raise env.error("%s %s" % (cfg, str(err)))
