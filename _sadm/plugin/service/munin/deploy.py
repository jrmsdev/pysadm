# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path, makedirs
from shutil import chown

from _sadm.plugin.utils.cmd import call, call_check

__all__ = ['deploy']

_dbdir = path.join(path.sep, 'srv', 'munin', 'db')

def deploy(env):
	if call('service cron status') == 0:
		call_check('service cron reload')
	else:
		call_check('service cron start')
	makedirs(_dbdir, mode = 0o755, exist_ok = True)
	chown(_dbdir, user = 'munin', group = 'munin')
	env.log("dbdir %s" % _dbdir)
	call_check('service munin start')
