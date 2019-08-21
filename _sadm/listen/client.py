# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log

__all__ = ['ListenClient']

class ListenClient(object):
	_url = None

	def __init__(self, url):
		log.debug("url %s" % url)
		self._url = url

	def exec(self, task, action, args):
		pass
