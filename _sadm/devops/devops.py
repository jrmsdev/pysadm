# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log
from _sadm.devops.wapp import wapp

__all__ = ['start']

def start():
	w = wapp.init()
	quiet = log.curLevel() == 'quiet'
	debug = wapp.config.getboolean('devops', 'debug', fallback = False)
	if debug:
		quiet = False
	port = wapp.config.getint('devops', 'port', fallback = 3110)
	return w.run(host = '127.0.0.1', port = port, debug = debug,
		reloader = debug, quiet = quiet)
