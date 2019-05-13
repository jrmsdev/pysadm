# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import route

from _sadm import log
from _sadm.web.tpl import template

@route('/<who>')
@template('index.html')
def index(who):
	log.debug("index %s" % who)
	return "hello %s" % who
