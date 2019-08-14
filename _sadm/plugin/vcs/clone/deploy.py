# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

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
