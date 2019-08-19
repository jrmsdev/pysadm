# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.listen.wapp import wapp

@wapp.route('/hook/bitbucket/push/<repo>')
def push(repo):
	return 'it works!!'
