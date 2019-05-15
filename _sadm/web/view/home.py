# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import route, view

from _sadm import log
from _sadm.web import tpl

@route('/')
@view('index.html')
@tpl.data('home')
def index():
	log.debug("index")
	return {}
