# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import request

from _sadm.listen.wapp import wapp

from .repo import WebhookRepo

__all__ = ['repo']

@wapp.route('/hook/<provider>/<name>/<action>', 'POST', name = 'hook.repo')
def repo(provider, name, action):
	repo = WebhookRepo(provider, name)
	repo.auth(request)
	repo.exec(request, action)
	return 'OK\n'
