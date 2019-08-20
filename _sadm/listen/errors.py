# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import response

from _sadm import log

__all__ = ['init']

def handler(code, error):
	log.debug("handler %d" % code)
	log.debug("%d - %s" % (error.status_code, error.status_line))
	argsLen = len(error.args)
	if argsLen >= 3:
		log.error("%s" % error.args[2])
	if argsLen >= 4:
		log.debug("%s" % error.args[3])
	response.headers['Content-Type'] = 'text/plain; charset=UTF-8'
	return "ERROR: %d" % code

def init(wapp):
	@wapp.error(500)
	def error_500(error):
		return handler(500, error)
