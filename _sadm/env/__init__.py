# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from os import path
from time import time

from _sadm import log, config, asset
from _sadm.configure import plugins
from _sadm.env import cmd
from _sadm.env.profile import Profile
from _sadm.errors import Error, EnvError

class Env(object):
	_name = None
	_cfgfile = None
	_profile = None
	_profName = None
	_logtag = None
	_run = None
	assets = None
	settings = None

	def __init__(self, profile, name):
		self._name = name
		self._profile = Profile(profile)
		self._profName = self._profile.name()
		self._logtag = ''
		self._run = {}
		if not self._name in config.listEnvs(self._profName):
			raise self.error('env not found')
		self._load()

	def _load(self):
		self.debug("load %s" % self._name)
		opt = "env.%s" % self._name
		fn = path.normpath(config.get(self._profName, opt).strip())
		if fn == '':
			raise self.error('config file not set')
		pdir = path.normpath(config.get(self._profName, 'dir'))
		if pdir == '':
			raise self.error("%s profile dir not set" % self._profName)
		pdir = path.abspath(pdir)
		rootdir = path.join(pdir, path.dirname(fn))
		self.assets = asset.Manager(rootdir)
		log.debug("assets %s" % rootdir)
		self._cfgfile = path.basename(fn)
		self._loadcfg()

	def _loadcfg(self):
		if self._cfgfile == '':
			raise self.error('config file not set')
		self.debug("cfgfile %s" % self._cfgfile)

	def configure(self):
		self.start('configure', self._cfgfile)
		self.settings = plugins.configure(self, self._cfgfile)
		self.end('configure')

	def name(self):
		return self._name

	def profile(self):
		return self._profName

	def _log(self, func, msg):
		func("%s/%s%s %s" % (self._profName, self._name, self._logtag, msg))

	def log(self, msg):
		self._log(log.msg, msg)

	def info(self, msg):
		self._log(log.info, msg)

	def warn(self, msg):
		self._log(log.warn, msg)

	def debug(self, msg):
		tag = "%s/%s%s" % (self._profName, self._name, self._logtag)
		log.debug("%s" % msg, depth = 4, tag = tag)

	def error(self, msg):
		self._log(log.error, msg)
		return EnvError(msg)

	def start(self, action, msg = ''):
		if self._run.get(action, None) is not None:
			raise self.error("%s action already started" % action)
		prev = self._logtag
		self._logtag = " %s" % action
		sep = ''
		if msg != '':
			sep = ' '
		self.info("start%s%s" % (sep, msg))
		self._run[action] = {'tag.prev': prev, 'start': time()}

	def end(self, action):
		if self._run.get(action, None) is None:
			raise self.error("%s action was not started" % action)
		self._run[action]['end'] = time()
		self.info("end (%fs)" % (self._run[action]['end'] - self._run[action]['start']))
		self._logtag = self._run[action]['tag.prev']

	def report(self, msg = 'done', startTime = None):
		actno = 0
		noend = []
		for action, d in self._run.items():
			actno += 1
			if d.get('end', None) is None:
				noend.append(action)
		took = ''
		if startTime is not None:
			took = " (%fs)" % (time() - startTime)
		self.info("%s %d/%d actions%s" % (msg, (actno - len(noend)), actno, took))
		if len(noend) > 0:
			raise self.error("not finished action(s): %s" % str(noend))

	@contextmanager
	def lock(self):
		try:
			yield _lock(self)
		finally:
			_unlock(self)

def run(profile, env, action):
	try:
		env = Env(profile, env)
		cmd.run(env, action)
	except EnvError:
		return 1
	except Error as err:
		log.error("%s" % err)
		return 2
	return 0

def _lock(env):
	env.debug('lock')
	return env

def _unlock(env):
	env.debug('unlock')
