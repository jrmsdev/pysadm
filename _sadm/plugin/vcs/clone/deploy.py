# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.utils.vcs import git

from .check import check

__all__ = ['deploy']

def deploy(env):
	status = check(env)
	for st, name, typ, repo in status:
		if st == 'MISS':
			_cloneRepo(env, name, typ, repo)
		else:
			_updateRepo(env, name, typ, repo)

def _cloneRepo(env, name, typ, repo):
	env.log("clone %s repo %s" % (typ, name))
	if typ == 'git':
		_gitClone(env, name, repo)

def _updateRepo(env, name, typ, repo):
	env.log("update %s repo %s" % (typ, name))
	if not repo['update']:
		return
	if typ == 'git':
		git.pull(repo['path'])

def _gitClone(env, name, repo):
	git.clone(repo['path'], repo['remote'], repo['branch'])
	if repo['checkout'] != '':
		git.checkout(repo['path'], repo['checkout'])
