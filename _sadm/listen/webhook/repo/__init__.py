# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.listen.exec import dispatch
from _sadm.listen.errors import error

from .provider.bitbucket import BitbucketProvider

__all__ = ['WebhookRepo']

_types = ['git']
_provider = {
	'bitbucket': BitbucketProvider,
}

class WebhookRepo(object):
	_prov = None

	def __init__(self, config, provider, name):
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
		fn = self._prov.task(task, req)
		dispatch(task, fn)
