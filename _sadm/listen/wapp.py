# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from _sadm import libdir, log
from _sadm.utils import path

__all__ = ['wapp']

wapp = bottle.Bottle()
bottle.TEMPLATE_PATH = []

_cfgfn = libdir.fpath('listen', 'wapp.conf')
wapp.config.load_config(_cfgfn)

_systemCfg = path.join(path.sep, 'etc', 'opt', 'sadm', 'listen.cfg')
if path.isfile(_systemCfg):
	wapp.config.load_config(_systemCfg)

log.init(wapp.config['sadm.log'])

for opt in wapp.config.keys():
	log.debug("config section %s" % opt)
	if opt.startswith('sadm.webhook.'):
		log.debug("enable %s" % opt)
		from _sadm.listen.webhook import WebhookPlugin
		wapp.install(WebhookPlugin())
