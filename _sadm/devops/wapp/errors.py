# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import response, HTTPError, request, HTTP_CODES, template

from _sadm import log

__all__ = ['init', 'error']

def _handler(code, error):
	log.debug("%d - %s" % (error.status_code, error.status_line))
	argsLen = len(error.args)
	if argsLen >= 3:
		log.error("%s %d - %s" % (request.remote_addr, code, error.args[2]))
		if argsLen >= 4:
			log.debug("%s" % error.args[3])
	else:
		log.error("%s %d - %s" % (request.remote_addr, code, request.path))
	response.headers['Content-Type'] = 'text/html; charset=UTF-8'
	return template('errors.html', error = error)

def init(wapp):
	@wapp.error(404)
	def error_404(error):
		return _handler(404, error)

	@wapp.error(500)
	def error_500(error):
		return _handler(500, error)

def error(code, msg):
	log.error("%s %d - %s" % (request.remote_addr, code, msg))
	return HTTPError(
		status = code,
		body = msg,
	)
