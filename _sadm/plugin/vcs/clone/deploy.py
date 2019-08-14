# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.utils.cmd import callCheck
from _sadm.utils.sh import chdir, getcwd

from .check import check

__all__ = ['deploy']

def deploy(env):
	status = check(env)
	for st, name, typ, repo in status:
		if st == 'MISS':
			_cloneRepo(env, name, typ, repo)

def _cloneRepo(env, name, typ, repo):
	if typ == 'git':
		_gitClone(env, name, repo)

def _gitClone(env, name, repo):
	env.log("clone git repo %s" % name)
	cmd = ['git', 'clone', '-b', repo['branch'], repo['remote'], repo['path']]
	callCheck(cmd)
	if repo['checkout'] != '':
		oldwd = getcwd()
		try:
			chdir(repo['path'])
			cmd = ['git', 'checkout', repo['checkout']]
			callCheck(cmd)
		finally:
			chdir(oldwd)
