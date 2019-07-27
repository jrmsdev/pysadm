# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from unittest.mock import patch

from _sadmtest.mock import utils

import _sadm.utils.cmd

@contextmanager
def deploy(pname, cfgfn):
	print('-- mock.plugin:', pname, cfgfn)
	try:
		m = utils.MockCmdProc()
		_sadm.utils.cmd.proc = m
		yield m
	finally:
		_sadm.utils.cmd.proc = _sadm.utils.cmd._ProcMan()
