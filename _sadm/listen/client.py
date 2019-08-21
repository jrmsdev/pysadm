# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json
from urllib.request import urlopen

from _sadm import log

__all__ = ['ListenClient']

class ListenClient(object):
	_url = None

	def __init__(self, url):
		log.debug("url %s" % url)
		self._url = self._path(url, '_')

	def _path(self, *parts):
		return '/'.join(parts)

	def _post(self, path, data):
		url = self._path(self._url, path)
		with urlopen(url, data = data) as resp:
			if resp.status != 200:
				log.error("%s returned: %d - %s" % (url, resp.status, resp.reason))

	def exec(self, task, action, args):
		path = self._path('exec', task, action)
		self._post(path, json.dumps(args).encode('UTF-8'))
