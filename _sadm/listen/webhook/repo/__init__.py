# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json

from _sadm import log
from _sadm.listen.exec import dispatch
from _sadm.listen.errors import error
from _sadm.utils import sh, path

from .provider.bitbucket import BitbucketProvider

__all__ = ['WebhookRepo']

_types = ['git']
_provider = {
	'bitbucket': BitbucketProvider,
}

class WebhookRepo(object):
	_prov = None
	_provName = None
	_repoName = None

	def __init__(self, config, provider, name):
		self._provName = provider
		self._repoName = name
		provClass = _provider.get(provider, None)
		if provClass is None:
			raise error(400, "webhook invalid provider: %s" % provider)
		sect = "sadm.webhook:%s" % name
		if not config.has_section(sect):
			raise error(400, "webhook %s repo not found: %s" % (provider, name))
		cfg = config[sect]
		self._prov = provClass(cfg)
		self._loadRepo(cfg, provider, name)

	def _loadRepo(self, cfg, provider, name):
		rProv = cfg.get('provider', fallback = '')
		if rProv != provider:
			raise error(400, "webhook %s repo %s invalid provider: %s" % (provider, name, rProv))
		rType = cfg.get('type', fallback = 'git')
		if not rType in _types:
			raise error(400, "webhook %s repo %s invalid type: %s" % (provider, name, rType))

	def auth(self, req):
		self._prov.auth(req)

	def exec(self, task, req):
		log.debug("req.body: %s" % req.body)
		if not req.body:
			raise error(400, "webhook %s repo %s empty body" % (self._provName, self._repoName))
		fn = self._reqSave(req.body)
		try:
			dispatch(task, fn)
		finally:
			path.unlink(fn)

	def _reqSave(self, body):
		obj = json.loads(body.read())
		data = json.dumps(obj)
		fn = None
		with sh.mktmp(prefix = __name__, suffix = '.json') as fh:
			fh.write(data)
			fn = fh.name()
		return fn
