# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__all__ = ['BitbucketProvider']

class BitbucketProvider(object):

	def auth(self, req, cfg, data): # FIXME
		pass

	def repoArgs(self, cfg, data):
		return {
			'repo.path': cfg.get('path'),
		}
