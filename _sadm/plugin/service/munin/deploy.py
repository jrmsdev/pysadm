# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.plugin.utils.cmd import call, call_check

__all__ = ['deploy']

def deploy(env):
	if call('service cron status') == 0:
		call_check('service cron reload')
	else:
		call_check('service cron start')
	call_check('service munin start')
