# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.devops.wapp.tpl import tpl

def test_init(devops_wapp):
	wapp = devops_wapp()
	with wapp.mock() as ctx:
		ctx.orig.tpl.parse('testing.html', tdata = None)
		ctx.bottle.template.assert_called_once()

def test_template():
	t = tpl.Template('testing.html', {})
	assert t.name == 'testing.html'
	assert t.data == {}
