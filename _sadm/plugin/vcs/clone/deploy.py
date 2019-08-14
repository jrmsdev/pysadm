# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__all__ = ['deploy']

def deploy(env):
	for opt in env.settings.options('vcs.clone'):
		print(opt)
