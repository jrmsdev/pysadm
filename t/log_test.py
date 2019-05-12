# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log

def test_log():
	assert log._getCaller(1).startswith('t/log_test.py:')
