# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.listen.errors import error

from .git import GitRepo
from .provider.bitbucket import BitbucketProvider

__all__ = ['WebhookRepo']

_type = {
	'git': GitRepo,
}
_provider = {
	'bitbucket': BitbucketProvider,
}

class WebhookRepo(object):
	_prov = None
	cmd = None

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
		typeClass = _type.get(rType, None)
		if typeClass is None:
			raise error(400, "webhook %s repo %s invalid type: %s" % (provider, name, rType))
		self.cmd = typeClass(cfg)
