# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.devops.wapp.tpl import tpl

__all__ = ['login']

def login():
	return tpl.parse('user/login.html')
