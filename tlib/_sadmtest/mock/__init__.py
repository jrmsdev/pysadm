# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from _sadmtest.mock import utils

@contextmanager
def deploy(pname, cfgfn):
	print('-- mock.plugin:', pname, cfgfn)
	try:
		m = utils.MockCmd()
		yield m
	finally:
		pass
