# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.devops.wapp import wapp
from _sadm.devops.wapp.auth import WebappAuth
from _sadm.devops.wapp.tpl import tpl

__all__ = ['login']

def login():
	auth = WebappAuth()
	auth.setup(wapp.config)
	return tpl.parse('user/login.html')
