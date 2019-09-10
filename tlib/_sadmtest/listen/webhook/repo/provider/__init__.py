# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__all__ = ['TestingProvider']

class TestingProvider(object):

	def auth(self, slug, req, cfg, obj):
		pass

	def validate(self, slug, cfg, obj):
		pass

	def repoArgs(self, slug, cfg, obj):
		return {}
