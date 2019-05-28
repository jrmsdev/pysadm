# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path
from subprocess import call, TimeoutExpired

from _sadm import log, libdir
from _sadm.errors import PluginScriptNotFound, PluginScriptNoExec, PluginScriptTimeout

__all__ = ['Scripts']

_TTL = 180

def _osdist():
	return 'debian' # FIXME

class Scripts(object):
	_dir = None

	def __init__(self, pname, dist = None):
		if dist is None:
			dist = _osdist()
		self._dir = libdir.path('scripts', dist, pname.replace('.', path.sep))
		log.debug("%s" % self._dir)

	def run(self, script, *args):
		spath = path.join(self._dir, script)
		log.debug("run %s %s" % (spath, args))
		s = _Script(spath, args)
		return s.dispatch()

class _Script(object):
	_cmd = None

	def __init__(self, script, *args):
		self._cmd = [script]
		self._cmd.extend(*args)

	def dispatch(self):
		try:
			return call(self._cmd, timeout = _TTL)
		except FileNotFoundError:
			raise PluginScriptNotFound(self._cmd[0])
		except PermissionError:
			raise PluginScriptNoExec(self._cmd[0])
		except TimeoutExpired:
			raise PluginScriptTimeout("%s after %s seconds" % (self._cmd[0], _TTL))