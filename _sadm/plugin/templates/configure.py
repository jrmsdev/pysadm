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
			src = cfg[s].get('src.path', fallback = '')
			if src == '':
				raise PluginError("template %s src.path not set" % name)
			dst = cfg[s].get('dst.path', fallback = '')
			if dst == '':
				raise PluginError("template %s dst.path not set" % name)
			if not env.assets.isfile(src):
				raise PluginError("template %s src.path %s: file not found" % (name, src))
			if not path.isabs(dst):
				raise PluginError("template %s dst.path %s: must be an absolute path" % (name, dst))
			args = _getargs(env, name, cfg[s])
			tpl.append((name, src, dst, args))
	env.session.set('templates.build', tpl)

def _getargs(env, name, cfg):
	args = {}
	for opt in cfg.keys():
		if opt == 'src.path' or opt == 'dst.path':
			continue
		args[opt] = cfg.get(opt)
	return args
