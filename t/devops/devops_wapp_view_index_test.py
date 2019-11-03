# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.devops.wapp.view import index

def test_handle(devops_wapp):
	wapp = devops_wapp()
	with wapp.mock() as ctx:
		index.handle(user = None)
		ctx.tpl.parse.assert_called_with('index', user = None)
