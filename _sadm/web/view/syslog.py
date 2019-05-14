# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import route, view
from _sadm import log

@route('/syslog')
@view('syslog.html')
def index():
	log.debug("index")
	return {}
