# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

# ~ import json
import sys # FIXME: only for debug

from os import path

from _sadm import config
from _sadm.configure import pluginsList, pluginInit, getPlugin
from _sadm.env.configure import Settings2

# load plugins
import _sadm.plugin.load

__all__ = ['configure']

def configure(env, cfgfile = None):
	if cfgfile is None:
		cfgfile = env.cfgfile()
	fn = path.join(env.rootdir(), cfgfile)
	env.log("%s" % fn)
	cfg = _getcfg(env, fn)
	_load(env, cfg)
	with env.assets.open(fn) as fh:
		_cfgread(env, env.settings2, fh)
	env.settings2.write(sys.stdout) # FIXME: only for debug

def _cfgread(env, cfg, fh):
	try:
		cfg.read_file(fh)
	except FileNotFoundError as err:
		raise env.error("%s" % err)

def _getcfg(env, fn):
	cfg = Settings2(env.profile(), env.name())
	with env.assets.open(fn) as fh:
		_cfgread(env, cfg, fh)
	n = cfg.get('default', 'name', fallback = None)
	if n != env.name():
		raise env.error("invalid config name '%s'" % n)
	return cfg

def _load(env, cfg, forcePlugins = None):
	env.debug("registered plugins %s" % ','.join([p for p in pluginsList()]))
	if forcePlugins is None:
		forcePlugins = {}
		for p in config.listPlugins(env.profile()):
			forcePlugins[p] = True
	env.debug("plugins force enable: %s" % ','.join([p for p in forcePlugins.keys()]))
	for p in pluginsList():
		ena = cfg.has_section(p)
		forceEna = forcePlugins.get(p, False)
		if ena or forceEna:
			env.debug("%s plugin enabled" % p)
			_initPlugin(env, pluginInit(p))
			_pluginConfigure(env, cfg, p)
		else:
			env.debug("%s plugin disabled" % p)

def _initPlugin(env, fn):
	env.debug("init %s" % fn)
	with open(fn, 'r') as fh:
		_cfgread(env, env.settings2, fh)

def _pluginConfigure(env, cfg, p):
	mod = getPlugin(p, 'configure')
	tag = "configure.%s" % p
	env.start(tag)
	mod.configure(env, cfg)
	env.end(tag)


















	# ~ cfg = _getcfg(env, cfgfile)
	# ~ data = _load(env, cfg)
	# ~ env.settings._data = data # FIXME: remove

# ~ def _getcfg(env, fn):
	# ~ with env.assets.open(fn) as fh:
		# ~ cfg = json.load(fh)
	# ~ n = cfg.get('name', '')
	# ~ if n != env.name():
		# ~ raise env.error("invalid config name '%s'" % n)
	# ~ return cfg

# ~ def _load(env, cfg, enabledPlugins = None):
	# ~ env.debug("registered plugins %s" % ','.join([p for p in pluginsList()]))
	# ~ if enabledPlugins is None:
		# ~ enabledPlugins = {}
		# ~ for p in config.listPlugins(env.profile()):
			# ~ enabledPlugins[p] = True
	# ~ env.debug("config enabled plugins: %s" % ','.join([p for p in enabledPlugins.keys()]))
	# ~ data = {}
	# ~ env.debug("data %s" % data)
	# ~ for p in pluginsList():
		# ~ env.debug("plugin %s" % p)
		# ~ cfgena = enabledPlugins.get(p, False)
		# ~ cfgdata = cfg.get(p, None)
		# ~ env.debug("cfgena %s" % cfgena)
		# ~ env.debug("cfgdata %s" % cfgdata)
		# ~ if cfgdata is None and not cfgena:
			# ~ env.debug("%s plugin not enabled" % p)
		# ~ else:
			# ~ # plugin enabled
			# ~ env.debug("plugin %s enabled" % p)
			# ~ pdata = pluginInit(env, p)
			# ~ env.debug("pdata %s" % pdata)
			# ~ data.update(pdata)
			# ~ env.settings.init(p, pdata)
			# ~ env.debug("data %s" % data)
			# ~ if cfgdata is not None:
				# ~ env.debug('update cfgdata')
				# ~ data.update({p: cfgdata})
				# ~ env.debug("data %s" % data)
			# ~ mod = getPlugin(p, 'configure')
			# ~ tag = "configure.%s" % p
			# ~ env.start(tag)
			# ~ moddata = {p: mod.configure(env)}
			# ~ env.debug("moddata %s" % moddata)
			# ~ data.update(moddata)
			# ~ env.debug("data %s" % data)
			# ~ env.end(tag)
	# ~ env.debug("data %s" % data)
	# ~ return data
