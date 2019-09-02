# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from contextlib import contextmanager

from _sadm.utils import sh
from _sadm.utils.cmd import callCheck

__all__ = ['clone', 'checkout', 'pull', 'deploy']

_configDone = False

def _configure():
	global _configDone
	if _configDone:
		return
	cmd = ['git', 'config', '--global', 'core.sshCommand',
		'ssh -n -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no']
	callCheck(cmd)
	_configDone = True

def clone(path, remote, branch):
	_configure()
	cmd = ['git', 'clone', '-b', branch, remote, path]
	callCheck(cmd)

@contextmanager
def _repoDir(path):
	_configure()
	oldwd = sh.getcwd()
	try:
		sh.chdir(path)
		yield
	finally:
		sh.chdir(oldwd)

def checkout(path, commit):
	with _repoDir(path):
		callCheck(['git', 'checkout', commit])

def pull(path):
	with _repoDir(path):
		callCheck(['git', 'pull'])

def deploy(path):
	pull(path)
	with _repoDir(path):
		pass
		# TODO: run .sadm/deploy.scripts
