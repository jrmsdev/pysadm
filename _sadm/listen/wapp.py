# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from _sadm import libdir, log, version
from _sadm.utils import path

__all__ = ['wapp', 'init']

wapp = bottle.Bottle()
bottle.TEMPLATE_PATH = []

_cfgfn = libdir.fpath('listen', 'wapp.conf')
wapp.config.load_config(_cfgfn)

def init():
	_systemCfg = path.join(path.sep, 'etc', 'opt', 'sadm', 'listen.cfg')
	if path.isfile(_systemCfg):
		wapp.config.load_config(_systemCfg)

	log.init(wapp.config['sadm.log'])
	log.debug(version.string('sadm'))

	for opt in wapp.config.keys():
		if opt.startswith('sadm.webhook.'):
			log.debug("enable %s" % opt)
			from _sadm.listen.webhook import WebhookPlugin
			wapp.install(WebhookPlugin())

	return wapp
