# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises
from _sadm.plugin import configure

def test_reg():
	configure.register(__name__)
	assert configure._reg['register_test'] == 'register_test'
	with raises(RuntimeError):
		configure.register(__name__)
	assert configure._reg == {
		'register_test': 'register_test',
		'sadm': '_sadm.plugin.sadm',
	}
