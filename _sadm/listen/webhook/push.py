# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.listen.wapp import wapp

__all__ = ['push']

@wapp.route('/hook/<provider>/<name>/push')
def push(repo, provider, name):
	return 'it works!!'
