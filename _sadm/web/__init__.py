# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle
from os import path

from _sadm import log

# load views
import _sadm.web.view.home

_srcdir = path.abspath(path.dirname(__file__))
_staticdir = path.join(_srcdir, 'static')

@bottle.route('/static/<filename:path>')
def static(filename):
	return bottle.static_file(filename, root = _staticdir, download = False)

def start(host, port, debug):
	htmldir = path.join(_srcdir, 'html')
	log.debug("start %s" % htmldir)
	bottle.TEMPLATE_PATH = [htmldir]
	bottle.run(host = host, port = port, reloader = debug,
		quiet = not debug, debug = False)
