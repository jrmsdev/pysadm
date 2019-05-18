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
	data = _load(env, cfgfile)
	return Settings(data)

def _load(env, fn):
	with env.assets.open(fn, 'r') as fh:
		data = json.load(fh)
	n = data.get('name', '')
	if n != env.name():
		raise env.error("invalid config name '%s'" % n)
	for p in pluginsList():
		env.log("%s" % p)
		pluginInit(env, p)
	return data
