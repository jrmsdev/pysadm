# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log
from _sadm.devops.wapp.static import static
from _sadm.devops.wapp.view import index

__all__ = ['init']

def init(wapp):
	wapp.route(r'/static/<filename:re:.*\..*>', 'GET', static.serve, name = 'static')
	wapp.route('/', 'GET', index.handle, name = 'index')
