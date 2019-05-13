# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import route, run

@route('/')
def index():
	return '<p>hello world!</p>'

def start(host, port):
	run(host = host, port = port)
