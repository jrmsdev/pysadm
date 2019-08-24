# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

def test_defaults(testing_wapp):
	wapp = testing_wapp('listen')
	assert wapp
