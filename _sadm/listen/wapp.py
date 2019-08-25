# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle
from configparser import ConfigParser, ExtendedInterpolation

from _sadm import libdir, log, version
from _sadm.listen import errors
from _sadm.utils import path

__all__ = ['wapp', 'config', 'init']

wapp = bottle.Bottle()

bottle.TEMPLATE_PATH = []
wapp.uninstall('template')
wapp.uninstall('json')

_cfgfn = libdir.fpath('listen', 'wapp.conf')
wapp.config.load_config(_cfgfn)

errors.init(wapp)

config = None
_cfgfn = path.join(path.sep, 'etc', 'opt', 'sadm', 'listen.cfg')

def _newConfig(fn):
	c = ConfigParser(
		defaults = None,
		allow_no_value = False,
		delimiters = ('=',),
		comment_prefixes = ('#',),
		strict = True,
		interpolation = ExtendedInterpolation(),
		default_section = 'default',
	)
	with open(fn, 'r') as fh:
		c.read_file(fh)
	return c

def init(cfgfn = _cfgfn):
	global config
	config = _newConfig(cfgfn)

	log.init(config.get('sadm', 'log', fallback = 'error'))
	log.debug(version.string('sadm-listen'))

	from _sadm.listen import handlers
	from _sadm.listen.plugin import HandlersPlugin
	wapp.install(HandlersPlugin())

	initDone = {}
	for sect in config.sections():

		if sect.startswith('sadm.webhook:'):
			if not initDone.get('webhook', False):
				log.debug('enable webhook')
				from _sadm.listen import webhook
				from _sadm.listen.plugin.webhook import WebhookPlugin
				wapp.install(WebhookPlugin())
				initDone['webhook'] = True

	return wapp
