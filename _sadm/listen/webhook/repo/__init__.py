# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json

from _sadm import log
from _sadm.listen.exec import dispatch
from _sadm.listen.errors import error
from _sadm.utils import sh, path

from .provider.bitbucket import BitbucketProvider

__all__ = ['WebhookRepo']

_validVCS = {
	'git': True,
}
_provider = {
	'bitbucket': BitbucketProvider(),
}

class WebhookRepo(object):
	_cfg = None
	_prov = None
	_provName = None
	_repoName = None
	_repoVCS = None

	def __init__(self, config, provider, name):
		self._provName = provider
		self._repoName = name
		prov = _provider.get(provider, None)
		if prov is None:
			raise error(400, "webhook invalid provider: %s" % provider)
		sect = "sadm.webhook:%s" % name
		if not config.has_section(sect):
			raise error(400, "webhook %s repo not found: %s" % (provider, name))
		self._cfg = config[sect]

		# TODO: check repo.path and other pre-fly checks

		self._prov = prov
		self._loadRepo(self._cfg, provider, name)

	def _loadRepo(self, cfg, provider, name):
		rProv = cfg.get('provider', fallback = 'none')
		if rProv != provider:
			raise error(400, "webhook %s repo %s invalid provider: %s" % (provider, name, rProv))
		vcs = cfg.get('vcs', fallback = 'git')
		if not _validVCS.get(vcs, False):
			raise error(400, "webhook %s repo %s invalid vcs: %s" % (provider, name, vcs))
		self._repoVCS = vcs

	def auth(self, req):
		self._prov.auth(req, self._cfg)

	def exec(self, req, action):
		log.debug("req.body: %s" % req.body)
		if not req.body:
			raise error(400, "webhook %s repo %s empty body" % (self._provName, self._repoName))

		# TODO: check self._cfg.getboolean(action... if disabled raise error 400

		reqfn = self._reqSave(req.body)
		try:
			args = {
				'request': reqfn,
				'repo.name': self._repoName,
				'repo.vcs': self._repoVCS,
				'repo.path': self._cfg.get('path'),
			}
			task = "webhook.repo.%s" % self._provName
			dispatch(task, action, args)
		finally:
			path.unlink(reqfn)

	def _reqSave(self, body):
		obj = json.loads(body.read())
		data = json.dumps(obj)
		fn = None
		with sh.mktmp(prefix = __name__, suffix = '.json') as fh:
			fh.write(data)
			fn = fh.name()
		return fn
