# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import route

@route('/')
def index():
	return 'hello world2!'
