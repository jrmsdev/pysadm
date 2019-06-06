# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.plugin.utils.cmd import call, call_check

__all__ = ['deploy']

def deploy(env):
	call_check('service munin-node stop')
	call_check('service munin-node start')
	call_check('service munin-node status')
