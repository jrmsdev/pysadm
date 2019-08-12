# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.utils.cmd import call, callCheck

_ctlcmd = ['systemctl', '--quiet', '--no-pager', '--no-legend', '--no-ask-password']

def _cmd(service, action, *args, check = True):
	cmd = []
	cmd.extend(_ctlcmd)
	cmd.extend(args)
	cmd.append(action)
	cmd.append(service)
	if check:
		return callCheck(cmd)
	return call(' '.join(cmd))

def status(service, *args):
	return _cmd(service, 'status', *args, check = False)

def start(service, *args):
	return _cmd(service, 'start', *args)

def stop(service, *args):
	return _cmd(service, 'stop', *args)

def restart(service, *args):
	return _cmd(service, 'restart', *args)

def reload(service, *args):
	return _cmd(service, 'reload', *args)
