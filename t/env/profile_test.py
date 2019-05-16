# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.env.profile import Profile

def test_profile():
	p = Profile('testing')
	assert p.name == 'testing'
