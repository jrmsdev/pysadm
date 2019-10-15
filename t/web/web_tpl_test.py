# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.web import tpl

def test_data():
	@tpl.data('testing')
	def tdata():
		return {'tdata': 'testing'}
	d = tdata()
	assert isinstance(d, dict)
