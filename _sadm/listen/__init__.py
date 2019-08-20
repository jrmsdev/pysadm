# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.listen import wapp

__all__ = ['start']

def start():
	app = wapp.init()
	debug = app.config['sadm.log'] == 'debug'
	host = app.config['sadm.listen.host']
	port = app.config['sadm.listen.port']
	return app.run(host = host, port = port, debug = debug,
		reloader = debug, quiet = not debug)
