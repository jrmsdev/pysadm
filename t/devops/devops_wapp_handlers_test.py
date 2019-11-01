# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from unittest.mock import call

from _sadm.devops.wapp import handlers
from _sadm.devops.wapp.view import index

def test_init(devops_wapp):
	wapp = devops_wapp()
	with wapp.mock() as ctx:
		handlers.init(ctx.wapp)
		assert ctx.wapp.route.mock_calls == [
			call('/', 'GET', index.handle, name = 'index'),
		]
