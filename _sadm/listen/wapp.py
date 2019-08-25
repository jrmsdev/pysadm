# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle
from configparser import ConfigParser, ExtendedInterpolation

from _sadm import libdir, log, version
from _sadm.listen import errors
from _sadm.utils import path

__all__ = ['wapp', 'config', 'init']

class Webapp(bottle.Bottle):

	@property
	def request(self):
		return bottle.request

	@property
	def response(self):
		return bottle.response

wapp = Webapp()
bottle.TEMPLATE_PATH = []

_cfgfn = libdir.fpath('listen', 'wapp.conf')
wapp.config.load_config(_cfgfn)

errors.init(wapp)

def _newConfig():
	return ConfigParser(
		defaults = None,
		allow_no_value = False,
		delimiters = ('=',),
		comment_prefixes = ('#',),
		strict = True,
		interpolation = ExtendedInterpolation(),
		default_section = 'default',
	)
config = _newConfig()

def init(cfgfn = None):
	if cfgfn is None: # pragma: no cover
		cfgfn = path.join(path.sep, 'etc', 'opt', 'sadm', 'listen.cfg')
	with open(cfgfn, 'r') as fh:
		config.read_file(fh)

	log.init(config.get('sadm', 'log', fallback = 'warn'))
	log.debug(version.string('sadm'))

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
