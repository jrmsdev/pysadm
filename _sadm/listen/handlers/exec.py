# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.listen.wapp import wapp

__all__ = ['exech']

@wapp.route('/_/exec', 'POST')
def exech():
	return 'OK\n'
