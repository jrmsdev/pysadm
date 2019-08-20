# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.listen.wapp import wapp

__all__ = ['start']

def start():
	debug = wapp.config['sadm.log'] == 'debug'
	return wapp.run(debug = debug, reloader = debug, quiet = not debug)
