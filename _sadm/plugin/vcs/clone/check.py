# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__all__ = ['check']

def check(env):
	repos = {}
	for opt in env.settings.options('vcs.clone'):
		items = opt.split('.')
		rn = items[0]
		k = '.'.join(items[1:])
		v = env.settings.get('vcs.clone', opt)
		if not rn in repos.keys():
			repos[rn] = {}
		repos[rn][k] = v
