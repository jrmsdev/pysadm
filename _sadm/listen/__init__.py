# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.listen.wapp import wapp

__all__ = ['start']

def start():
	debug = wapp.config['sadm.log'] == 'debug'
	host = wapp.config['sadm.listen.host']
	port = wapp.config['sadm.listen.port']
	return wapp.run(host = host, port = port, debug = debug,
		reloader = debug, quiet = not debug)
