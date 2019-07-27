# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager
from unittest.mock import patch

from _sadmtest.mock.utils.cmd import MockCmdProc
from _sadmtest.mock.utils.sh import MockShUtil

import _sadm.utils.cmd
import _sadm.utils.sh

class Manager(object):
	pass

@contextmanager
def deploy(pname, cfg):
	print('-- mock.plugin:', pname, cfg)
	try:
		m = Manager()
		_sadm.utils.cmd.proc = MockCmdProc(cfg)
		_sadm.utils.sh.shutil = MockShUtil(cfg)
		yield m
	finally:
		_sadm.utils.cmd.proc = _sadm.utils.cmd._ProcMan()
		_sadm.utils.sh.shutil = _sadm.utils.sh._ShUtil()
