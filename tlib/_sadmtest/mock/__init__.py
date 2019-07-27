# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from unittest.mock import patch

from _sadmtest.mock.utils.cmd import MockCmdProc

import _sadm.utils.cmd

@contextmanager
def deploy(pname, cfg):
	print('-- mock.plugin:', pname, cfg)
	try:
		m = MockCmdProc(cfg)
		_sadm.utils.cmd.proc = m
		yield m
	finally:
		_sadm.utils.cmd.proc = _sadm.utils.cmd._ProcMan()
