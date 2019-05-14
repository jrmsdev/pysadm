# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import route, view
from _sadm import log
from _sadm.web import tpl

@route('/syslog')
@view('syslog.html')
@tpl.data('syslog')
def index():
	log.debug("index")
	return {}
