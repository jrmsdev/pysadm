# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.listen.errors import error

__all__ = ['BitbucketProvider']

class BitbucketProvider(object):

	def auth(self, slug, req, cfg, data):
		for arg in ('name', 'uuid'):
			self._authRepo(arg, slug, cfg, data)

	def _authRepo(self, opt, slug, cfg, data):
		val = cfg.get("auth.%s" % opt)
		if val:
			try:
				x = data['repository'][opt]
				if x != val:
					raise error(403, "%s forbidden: %s %s" % (slug, opt, x))
			except KeyError:
				raise error(403, "%s forbidden: no %s" % (slug, opt))

	def validate(self, slug, cfg, data):
		for arg in ('nickname', 'uuid'):
			self._validUser(arg, slug, cfg, data)

	def _ls(self, val):
		r = []
		for l in val.splitlines():
			for x in l.split():
				r.append(x)
		return r

	def _validUser(self, opt, slug, cfg, data):
		val = cfg.get("auth.user.%s" % opt)
		if val:
			try:
				x = data['actor'][opt]
				if not x in self._ls(val):
					raise error(304, "%s no action: user %s %s" % (slug, opt, x))
			except KeyError:
				raise error(403, "%s forbidden: no user %s" % (slug, opt))

	def repoArgs(self, slug, cfg, data):
		return {
			'repo.path': cfg.get('path'),
		}
