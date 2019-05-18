# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from time import time

from _sadm import log, config
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
	settings = None

	def __init__(self, profile, name):
		self._name = name
		self._profile = Profile(profile)
		self._profName = self._profile.name()
		self._logtag = ''
		self._run = {}
		self._load()

	def _load(self):
		self.debug('load')
		if not self._name in config.listEnvs(self._profName):
			raise self.error('env not found')
		opt = "env.%s" % self._name
		self._cfgfile = config.get(self._profName, opt)
		self._cfgfile = self._cfgfile.strip()
		self._loadcfg()
		self._loadSettings()

	def _loadcfg(self):
		if self._cfgfile == '':
			raise self.error('config file not set')
		self.debug("cfgfile %s" % self._cfgfile)

	def _loadSettings(self):
		self.settings = plugins.configure(self, self._cfgfile)

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

	def start(self, action):
		if self._run.get(action, None) is not None:
			raise self.error("%s action already started" % action)
		prev = self._logtag
		self._logtag = "[%s]" % action
		self.info('start')
		self._run[action] = {'tag.prev': prev, 'start': time()}

	def end(self, action):
		if self._run.get(action, None) is None:
			raise self.error("%s action was not started" % action)
		self._run[action]['end'] = time()
		self.info("end (%fs)" % (self._run[action]['end'] - self._run[action]['start']))
		self._logtag = self._run[action]['tag.prev']

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
