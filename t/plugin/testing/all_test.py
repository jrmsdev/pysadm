# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

def test_testing_plugin(testing_plugin):
	p = testing_plugin('testing', ns = '_sadmtest')
	assert p.configure()
