# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import version

def test_get():
	assert version.get() == 'master'

def test_build():
	assert version.build() == 'devel'

def test_string():
	assert version.string() == '%(prog)s version master (build devel)'
