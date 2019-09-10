# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__all__ = ['TestingProvider']

class TestingProvider(object):

	def auth(self, slug, req, cfg, obj):
		return True

	def repoArgs(self, slug, cfg, obj):
		return {}
