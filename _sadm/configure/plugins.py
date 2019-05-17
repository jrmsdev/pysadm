# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json
from os import path

from _sadm import config
from _sadm.env.settings import Settings
from _sadm.configure import pluginsList

# load plugins
import _sadm.plugin

def configure(env, cfgfile):
	fn = _getFilename(env, cfgfile)
	data = _load(env, fn)
	return Settings(data)

def _getFilename(env, cfgfile):
	pdir = config.get(env.profile(), 'dir')
	pdir = pdir.strip()
	if pdir == '':
		raise env.error("%s profile dir not set" % self._profile)
	return path.join(path.normpath(pdir), cfgfile)

def _load(env, fn):
	env.debug("load %s" % fn)
	with open(fn, 'r') as fh:
		data = json.load(fh)
	n = data.get('name', '')
	if n != env.name():
		raise env.error("invalid config name '%s'" % n)
	for p in pluginsList():
		env.debug("init %s" % p)
	return data
