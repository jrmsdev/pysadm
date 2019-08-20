# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from . import bitbucket

__all__ = ['WebhookPlugin']

class WebhookPlugin(object):
	name = 'sadm.webhook'

	def setup(self, wapp):
		pass
