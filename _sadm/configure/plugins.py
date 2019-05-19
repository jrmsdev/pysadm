# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json
from os import path

from _sadm import config
from _sadm.env.settings import Settings
from _sadm.configure import pluginsList, pluginInit, getPlugin

# load plugins
import _sadm.plugin

__all__ = ['configure']

def configure(env, cfgfile = None):
	if cfgfile is None:
		cfgfile = env.cfgfile()
	env.log("%s" % path.join(env.rootdir(), cfgfile))
	cfg = _getcfg(env, cfgfile)
	data = _load(env, cfg)
	return Settings(data)

def _getcfg(env, fn):
	with env.assets.open(fn) as fh:
		cfg = json.load(fh)
	n = cfg.get('name', '')
	if n != env.name():
		raise env.error("invalid config name '%s'" % n)
	return cfg

def _load(env, cfg, enabledPlugins = None):
	env.debug("registered plugins %s" % ','.join([p for p in pluginsList()]))
	if enabledPlugins is None:
		enabledPlugins = {}
		for p in config.listPlugins(env.profile()):
			enabledPlugins[p] = True
	env.debug("config enabled plugins: %s" % ','.join([p for p in enabledPlugins.keys()]))
	data = {}
	env.debug("data %s" % data)
	for p in pluginsList():
		env.debug("plugin %s" % p)
		cfgena = enabledPlugins.get(p, False)
		cfgdata = cfg.get(p, None)
		env.debug("cfgena %s" % cfgena)
		env.debug("cfgdata %s" % cfgdata)
		if cfgdata is None and not cfgena:
			env.debug("%s plugin not enabled" % p)
		else:
			# plugin enabled
			env.debug("plugin %s enabled" % p)
			pdata = pluginInit(env, p)
			env.debug("pdata %s" % pdata)
			data.update(pdata)
			env.debug("data %s" % data)
			if cfgdata is not None:
				env.debug('update cfgdata')
				data.update({p: cfgdata})
				env.debug("data %s" % data)
			mod = getPlugin(p, 'configure')
			tag = "configure.%s" % p
			env.start(tag)
			moddata = {p: mod.configure(env)}
			env.debug("moddata %s" % moddata)
			data.update(moddata)
			env.debug("data %s" % data)
			env.end(tag)
	env.debug("data %s" % data)
	return data

class _Data(object):
	pass
