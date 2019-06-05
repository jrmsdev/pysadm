# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import subprocess as proc

from _sadm.errors import PluginCommandError

__all__ = ['call']

def call(cmd):
	shell = False
	if isinstance(cmd, str):
		shell = True
	return proc.call(cmd, shell = shell)

def call_check(cmd):
	shell = False
	if isinstance(cmd, str):
		shell = True
	try:
		return proc.check_call(cmd, shell = shell)
	except proc.CalledProcessError as err:
		raise PluginCommandError(str(err))
