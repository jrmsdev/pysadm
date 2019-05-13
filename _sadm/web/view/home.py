# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import route, view

from _sadm import log, version

@route('/')
@view('index.html')
def index():
	log.debug("index")
	return {}

@route('/about')
@view('about.html')
def about():
	log.debug("about")
	return {'version': version.get()}
