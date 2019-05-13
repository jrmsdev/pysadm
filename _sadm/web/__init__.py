# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import run

# load views
import _sadm.web.view.home

def start(host, port, debug):
	run(host = host, port = port, reloader = debug,
		quiet = not debug, debug = False)
