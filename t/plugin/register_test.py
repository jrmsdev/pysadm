# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises
from _sadm.plugin import configure

def test_reg():
	assert configure._reg == {}
	configure.register('plugin')
	assert configure._reg == {'plugin': True}
	with raises(RuntimeError):
		configure.register('plugin')
	assert configure._reg == {'plugin': True}
