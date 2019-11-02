# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from _sadm.devops.wapp import sess
from _sadm.devops.wapp.tpl import tpl

__all__ = ['login']

def login():
	s = sess.check(bottle.request)
	if not s:
		s = sess.new(bottle.response)
	return tpl.parse('user/login')
