# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from .check import check

from _sadm.plugin.utils.cmd import call, call_check

__all__ = ['deploy']

def deploy(env):
	if env.settings.getboolean('os.pkg', 'update'):
		env.log('update')
		_update()
	for diff in check(env):
		act, opt, pkg = diff
		env.log("%s %s" % (opt, pkg))
		if act == 'remove':
			_remove(pkg)
		elif act == 'install':
			_install(pkg)
		elif act == 'prune':
			_prune(pkg)

def _update():
	call_check(['apt-get', 'update'])

def _remove(pkg):
	call_check(['apt-get', 'autoremove', '-yy', '--purge', pkg])

def _install(pkg):
	call_check(['apt-get', 'install', '-yy', '--purge', '--no-install-recommends', pkg])

def _prune(pkg):
	call_check(['apt-get', 'autoremove', '-yy', '--purge', pkg])
