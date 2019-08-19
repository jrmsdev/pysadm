# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle
from _sadm import libdir

__all__ = ['wapp']

wapp = bottle.Bottle()
bottle.TEMPLATE_PATH = []

_cfgfn = libdir.fpath('listen', 'wapp.conf')
wapp.config.load_config(_cfgfn)
