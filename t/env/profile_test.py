# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

def test_profile(testing_profile):
	p = testing_profile
	assert p.name == 'testing'
