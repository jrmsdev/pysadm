# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from collections import deque
from os import path, chdir, getcwd

__all__ = ['check', 'getRepo']

_OPTIONS = (
	('type', 'git'),
	('remote', ''),
	('branch', 'master'),
	('checkout', ''),
	('path', ''),
)

def check(env):
	status = deque()
	repos = _getRepos(env)
	for name, repo in repos.items():
		typ = repo['type']
		env.log("check %s repo %s" % (typ, name))
		rpath = path.abspath(repo['path'])
		if not path.isdir(rpath):
			env.error("repo %s dir %s not found" % (name, rpath))
			status.append(('MISS', name, typ, repo))
			continue
		oldwd = getcwd()
		try:
			chdir(rpath)
			env.log("repo %s dir %s" % (name, rpath))
			if typ == 'git':
				_gitCheck(env, status, name, repo)
		except Exception as err:
			raise env.error("%s" % err)
		finally:
			chdir(oldwd)
	return status

def getRepo(env, name):
	repo = {}
	sect = "vcs.repo.%s" % name
	for key, defval in _OPTIONS:
		repo[key] = env.settings.get(sect, key, fallback = defval)
	return repo

def _getRepos(env):
	repos = {}
	for sect in env.settings.sections():
		if sect.startswith('vcs.repo.'):
			rn = sect.replace('vcs.repo.', '', 1)
			# override if already defined
			repos[rn] = getRepo(env, rn)
	return repos

def _gitCheck(env, status, name, repo): # TODO!!
	pass
