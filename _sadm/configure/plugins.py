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
	if enabledPlugins is None:
		enabledPlugins = {}
		for p in config.listPlugins(env.profile()):
			enabledPlugins[p] = True
	env.debug("config enabled plugins: %s" % ','.join([p for p in enabledPlugins.keys()]))
	data = {}
	for p in pluginsList():
		cfgena = enabledPlugins.get(p, False)
		cfgdata = cfg.get(p, None)
		if cfgdata is None and not cfgena:
			env.debug("%s plugin not enabled" % p)
		else:
			# plugin enabled
			data.update(pluginInit(env, p))
			if cfgdata is not None:
				data.update({p: cfgdata})
			mod = getPlugin(p, 'configure')
			tag = "configure.%s" % p
			env.start(tag)
			data.update({p: mod.configure(env, data)})
			env.end(tag)
	return data
