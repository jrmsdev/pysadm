# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.listen.webhook.handlers import repo

def test_hook_push(listen_wapp):
	wapp = listen_wapp()
	# ~ wapp.POST('bitbucket_push', repo, 'bitbucket', 'testing', 'push')
