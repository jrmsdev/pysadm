# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__all__ = ['configure']

def configure(env, cfg):
	for opt in cfg.options('vcs.clone'):
		if opt.endswith('.remote'):
			url = cfg.get('vcs.clone', opt, fallback = '')
			url = url.strip()
			if url == '':
				raise env.error("vcs.clone %s is empty" % opt)
			repo = opt.split('.')[0].strip()
			_configRepo(env, cfg, repo, url)

def _configRepo(env, cfg, repo, url):
	env.settings.merge(cfg, 'vcs.clone', (
		"%s.type" % repo,
		"%s.remote" % repo,
		"%s.branch" % repo,
		"%s.checkout" % repo,
	))
