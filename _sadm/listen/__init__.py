# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log
from _sadm.listen import wapp

__all__ = ['start']

def start():
	w = wapp.init()
	debug = log.curLevel('debug')
	host = wapp.config.get('sadm.listen', 'host', fallback = '127.0.0.1')
	port = wapp.config.getint('sadm.listen', 'port', fallback = 3666)
	return w.run(host = host, port = port, debug = debug,
		reloader = debug, quiet = not debug)