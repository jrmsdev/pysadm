# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from _sadm.devops.wapp import sess
from _sadm.devops.wapp.errors import error
from _sadm.devops.wapp.tpl import tpl

__all__ = ['login']

def login():
	req = bottle.request
	resp = bottle.response
	s = sess.check(req)
	if req.method == 'POST':
		if not s:
			return error(400, 'session cookie not found')
	else:
		if not s:
			s = sess.new(resp)
		return tpl.parse('user/login')
