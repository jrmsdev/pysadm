# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadmtest.wapp import TestingWebapp

__all__ = ['WebApp']

class WebApp(TestingWebapp):
	name = 'web'

	def __enter__(self):
		print("web app init %s" % self.cfgfn)
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		print("web app exit %s" % self.profile)
