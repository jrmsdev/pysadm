# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.errors import PluginError
from _sadm.utils import path

__all__ = ['configure']

def configure(env, cfg):
	if not cfg.getboolean('templates', 'enable', fallback = False):
		return
	tpl = []
	for s in cfg.sections():
		if s.startswith('template:'):
			name = s.split(':')[1]
			name = name.strip()
			if name == '':
				raise PluginError('template name is empty')
			src = cfg[s].get('src', fallback = '')
			if src == '':
				raise PluginError("template %s src filename not set" % name)
			dst = cfg[s].get('dst', fallback = '')
			if dst == '':
				raise PluginError("template %s dst filename not set" % name)
			if not env.assets.isfile(src):
				raise PluginError("template %s src %s: file not found" % (name, src))
			if not path.isabs(dst):
				raise PluginError("template %s dst %s: must be an absolute path" % (name, dst))
			tpl.append((name, src, dst))
	env.session.set('templates.build', tpl)
