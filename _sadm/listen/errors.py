# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import response, HTTPError, request

from _sadm import log

__all__ = ['init', 'error']

def handler(code, error):
	log.debug("handler %d" % code)
	log.debug("%d - %s" % (error.status_code, error.status_line))
	argsLen = len(error.args)
	if argsLen >= 3:
		log.error("%s %d - %s" % (request.remote_addr, code, error.args[2]))
		if argsLen >= 4:
			log.debug("%s" % error.args[3])
	else:
		log.error("%s %d - %s" % (request.remote_addr, code, request.path))
	response.headers['Content-Type'] = 'text/plain; charset=UTF-8'
	return "ERROR: %d" % code

def init(wapp):

	@wapp.error(500)
	def error_500(error):
		return handler(500, error)

	@wapp.error(400)
	def error_400(error):
		return handler(400, error)

	@wapp.error(404)
	def error_404(error):
		return handler(404, error)

def error(code, msg):
	log.error("%s %d - %s" % (request.remote_addr, code, msg))
	return HTTPError(
		status = code,
		body = msg,
	)
