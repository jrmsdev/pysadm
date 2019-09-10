# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.listen.errors import error

__all__ = ['BitbucketProvider']

class BitbucketProvider(object):

	def auth(self, slug, req, cfg, data):
		self._authData(slug, req, cfg, data)
		return True

	def _authData(self, slug, req, cfg, data):
		name = cfg.get('auth.name')
		if name != '':
			try:
				if name != data['repository']['name']:
					error(403, "%s forbidden: invalid repository %s" % (slug,
						data['repository']['name']))
			except KeyError:
				error(403, "%s forbidden: no repository name" % slug)

	def repoArgs(self, slug, cfg, data):
		return {
			'repo.path': cfg.get('path'),
		}
