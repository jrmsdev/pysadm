# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json
from os import path
from importlib import import_module

try:
	# python >=3.5
	from json.decoder import JSONDecodeError as jsonError
except ImportError: # pragma: no cover
	# python 3.4
	jsonError = ValueError

from _sadm.errors import PluginError

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

def getPlugin(name, mod):
	p = _reg.get(name, None)
	if p is None:
		raise PluginError("%s plugin not found" % name)
	try:
		mod = import_module("%s.%s" % (p['name'], mod))
	except ModuleNotFoundError:
		raise PluginError("%s plugin %s not implemented!" % (name, mod))
	return mod
