# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

def test_data(testing_webapp):
	wapp = testing_webapp('tpl')
	with wapp.mock() as ctx:
		@ctx.orig.tpl.data('testing')
		def tdata():
			return {'tdata': 'testing'}
		d = tdata()
		assert isinstance(d, dict)
