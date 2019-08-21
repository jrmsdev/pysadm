# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__all__ = ['BitbucketProvider']

class BitbucketProvider(object):

	def auth(self, req, cfg): # FIXME
		pass

	def taskArgs(self, obj, cfg):
		return {
			'repo.vcs': cfg.get('vcs'),
			'repo.path': cfg.get('path'),
		}

	def hook(self, action, args):
		pass
