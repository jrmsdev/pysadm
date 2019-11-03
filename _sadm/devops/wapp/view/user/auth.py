# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from _sadm.devops.wapp import cfg, sess
from _sadm.devops.wapp.auth import WebappAuth
from _sadm.devops.wapp.errors import error
from _sadm.devops.wapp.tpl import tpl

__all__ = ['login']

def login():
	req = bottle.request
	resp = bottle.response
	cookie = sess.cookie(req)
	if req.method == 'POST':
		if not cookie:
			return error(400, 'session cookie not found')
		auth = WebappAuth(cfg.config)
	else:
		if not cookie:
			sess.new(resp)
		return tpl.parse('user/login')
