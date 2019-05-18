# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises
from os import path
from _sadm.asset import Manager

def test_manager():
	m = Manager('tdata')
	assert m._dir.endswith(path.join('pysadm', 'tdata'))
	with m.open('sadm.cfg') as fh:
		fh.close()
	with raises(FileNotFoundError):
		m.open('nofile')