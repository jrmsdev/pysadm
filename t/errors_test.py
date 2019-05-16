# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.errors import Error

def test_error():
	err = Error('errType', 'errMsg')
	assert err == Error('errType', 'errMsg')
	assert str(err) == 'errType: errMsg'
	assert repr(err) == '<sadm.errType: errMsg>'
