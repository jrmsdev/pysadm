# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

def test_static(testing_webapp):
	wapp = testing_webapp('app')
	with wapp.mock() as ctx:
		pass
