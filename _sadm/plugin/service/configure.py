# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from _sadm import libdir
from _sadm.env.service import Service

__all__ = ['configure']

def configure(env, cfg):
	env.settings.merge(cfg, 'service', (
		'config.dir',
		'enable',
	))
	_loadEnabled(env)

def _loadEnabled(env):
	fn = 'service.conf'
	cfgdir = env.settings.get('service', 'config.dir', fallback = 'service')
	for s in env.settings.getlist('service', 'enable'):
		env.log("enable %s" % s)
		libfn = libdir.fpath('services', s, fn)
		libok = _loadConfig(env, libfn)
		sfn = env.assets.rootdir(cfgdir, s, fn)
		sok = _loadConfig(env, sfn)
		if not sok and not libok:
			raise env.error("%s file not found" % sfn)

def _loadConfig(env, fn):
	ok = False
	env.debug("load %s" % fn)
	if path.isfile(fn):
		Service(fn)
		ok = True
	else:
		env.debug("%s file not found" % fn)
	return ok
