# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

def test_hook_push(listen_wapp):
	with listen_wapp(profile = 'bitbucket') as wapp:
		wapp.POST('bitbucket_push', 'hook.repo', 'bitbucket', 'testing', 'push')
	assert wapp.response == 'OK'
