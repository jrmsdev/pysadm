# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from collections import deque, namedtuple
from importlib import import_module
from os import path

try:
	# python >= 3.6
	importError = ModuleNotFoundError
except NameError: # pragma: no cover
	# python 3.4 and 3.5
	importError = Exception

from _sadm import log
from _sadm.errors import PluginError

__all__ = ['register', 'getPlugin', 'pluginList']

_reg = {}
_order = deque()

Plugin = namedtuple('Plugin', ('name', 'fullname', 'config', 'meta', 'mod'))

def register(name, filename):
	global _next
	n = name.replace('_sadm.plugin.', '')
	if _reg.get(n, None) is not None:
		raise RuntimeError("plugin %s already registered" % name)
	srcdir = path.realpath(path.dirname(filename))
	cfgfn = path.join(srcdir, 'config.ini')
	metafn = path.join(srcdir, 'meta.json')
	_reg[n] = {
		'name': name,
		'distname': _distname(srcdir, name),
		'config': cfgfn,
		'meta': metafn,
	}
	_order.append(n)

def _distname(srcdir, name):
	dist = 'debian' # FIXME
	if path.isfile(path.join(srcdir, dist, '__init__.py')):
		return '.'.join([name, dist])
	return ''

def pluginsList(revert = False):
	if revert:
		for p in reversed(_order):
			yield p
	else:
		for p in _order:
			yield p

def getPlugin(name, mod):
	p = _reg.get(name, None)
	if p is None:
		raise PluginError("%s plugin not found" % name)
	pkg = p['name']
	if p['distname'] != '':
		pkg = p['distname']
	try:
		mod = import_module("%s.%s" % (pkg, mod))
	except importError as err:
		log.debug("%s" % err)
		raise PluginError("%s plugin %s not implemented!" % (name, mod))
	return Plugin(name = name, fullname = pkg, config = p['config'],
		meta = p['meta'], mod = mod)
