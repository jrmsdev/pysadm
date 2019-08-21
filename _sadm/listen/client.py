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
		self._url = url

	def _path(self, *parts):
		return '/'.join(parts)

	def _post(self, path, data):
		url = self._path(self._url, path)
		try:
			with urlopen(url, data) as resp:
				if resp.status != 200:
					log.error("%s returned: %d - %s" % (url, resp.status, resp.reason))
		except Exception as err:
			log.error("%s - %s" % (url, err))

	def exec(self, task, action, args):
		log.debug("exec: %s %s" % (task, action))
		path = self._path('_', 'exec', task, action)
		self._post(path, json.dumps(args).encode('UTF-8'))
