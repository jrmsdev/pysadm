# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path
from _sadm.configure import getPlugin

_srcdir = path.dirname(path.dirname(path.dirname(__file__)))

class Plugin(object):
	__p = None

	def __init__(self, name, ns = '_sadm'):
		self.__p = getPlugin(name, 'configure')
		assert self.__p.name == name, \
			"plugin %s name error: %s" % (name, self.__p.name)
		assert self.__p.fullname == "%s.plugin.%s" % (ns, name), \
			"plugin %s fullname error: %s" % (name, self.__p.fullname)
		assert self.__p.config == path.join(_srcdir, ns,
			'plugin', name, 'config.ini'), \
			"plugin %s config error: %s" % (name, self.__p.config)
		assert self.__p.meta == path.join(_srcdir, ns,
			'plugin', name, 'meta.json'), \
			"plugin %s meta file error: %s" % (name, self.__p.meta)
