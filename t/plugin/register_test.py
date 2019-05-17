# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises
from _sadm.plugin import configure

def test_reg():
	assert configure._reg == {}
	configure.register('_sadm.plugin.test')
	assert configure._reg == {'test': '_sadm.plugin.test'}
	with raises(RuntimeError):
		configure.register('_sadm.plugin.test')
	assert configure._reg == {'test': '_sadm.plugin.test'}
