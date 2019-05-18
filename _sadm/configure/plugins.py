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

def _load(env, cfg):
	d = {}
	for p in pluginsList():
		env.log("plugin %s" % p)
		d.update(pluginInit(env, p))
	return d
