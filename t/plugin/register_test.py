# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from pytest import raises
from os import path

from _sadm import configure

expectPlugins = {
	0: 'sadm',
	1: 'os',
	2: 'testing',
}
