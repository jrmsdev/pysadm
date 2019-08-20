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

def init(cfgfn = None):
	if cfgfn is None:
		cfgfn = path.join(path.sep, 'etc', 'opt', 'sadm', 'listen.cfg')
	if path.isfile(cfgfn):
		wapp.config.load_config(cfgfn)

	log.init(wapp.config['sadm.log'])
	log.debug(version.string('sadm'))

	initDone = {}

	for opt in wapp.config.keys():
		if opt.startswith('sadm.webhook.'):
			if not initDone.get('webhook', False):
				log.debug('enable webhook')
				from _sadm.listen import webhook
				webhook.init(wapp)
				initDone['webhook'] = True

	return wapp
