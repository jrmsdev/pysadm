# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json
from os import path

from _sadm import config
from _sadm.env.settings import Settings
from _sadm.configure import pluginsList, pluginInit

# load plugins
import _sadm.plugin

def configure(env, cfgfile):
	env.start('configure', cfgfile)
	cfg = _getcfg(env, cfgfile)
	data = _load(env, cfg)
	env.end('configure')
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
			env.log("plugin %s" % p)
			data.update(pluginInit(env, p))
			if cfgdata is not None:
				data.update({p: cfgdata})
		# TODO: run pmod.configure(data)
	return data
