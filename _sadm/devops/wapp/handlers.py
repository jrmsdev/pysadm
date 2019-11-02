# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log
from _sadm.devops.wapp.static import static
from _sadm.devops.wapp.view import index
from _sadm.devops.wapp.view.user import auth

__all__ = ['init']

def init(wapp):
	wapp.route(r'/static/<filename:re:.*\..*>', 'GET', static.serve,
		name = 'static', skip = ['sadm.devops.auth'])
	wapp.route('/', 'GET', index.handle, name = 'index')

	wapp.route('/user/login', ['GET', 'POST'], auth.login,
		name = 'user.login', skip = ['sadm.devops.auth'])
