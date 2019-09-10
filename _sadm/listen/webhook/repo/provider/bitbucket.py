# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.listen.errors import error

__all__ = ['BitbucketProvider']

class BitbucketProvider(object):

	def auth(self, slug, req, cfg, data):
		for arg in ('name', 'uuid'):
			self._authRepo(arg, slug, req, cfg, data)
		for arg in ('nickname', 'uuid'):
			self._authUser(arg, slug, req, cfg, data)
		return True

	def _authRepo(self, opt, slug, req, cfg, data):
		val = cfg.get("auth.%s" % opt)
		if val != '':
			try:
				x = data['repository'][opt]
				if val != x:
					error(403, "%s forbidden: %s %s" % (slug, opt, x))
			except KeyError:
				error(403, "%s forbidden: no %s" % (slug, opt))

	def _authUser(self, opt, slug, req, cfg, data):
		val = cfg.get("auth.user.%s" % opt)
		if val != '':
			try:
				x = data['actor'][opt]
				if val != x:
					error(403, "%s forbidden: user %s %s" % (slug, opt, x))
			except KeyError:
				error(403, "%s forbidden: no user %s" % (slug, opt))

	def repoArgs(self, slug, cfg, data):
		return {
			'repo.path': cfg.get('path'),
		}
