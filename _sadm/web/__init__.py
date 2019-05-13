# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle
from os import path

from _sadm import log

# load views
import _sadm.web.view.home

def start(host, port, debug):
	htmldir = path.join(path.dirname(__file__), 'html')
	log.debug("start %s" % htmldir)
	bottle.TEMPLATE_PATH = [htmldir]
	bottle.run(host = host, port = port, reloader = debug,
		quiet = not debug, debug = False)
