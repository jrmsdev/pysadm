# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.utils import systemd

__all__ = ['build']

def build(env):
	for s in env.settings.sections():
		if s.startswith('docker-compose:'):
			name = s.replace('docker-compose:', '', 1).strip()
			if name == '':
				raise env.error('docker-compose name is empty')
			cfg = env.settings[s]
			_composeConfigure(env, name, cfg)

def _composeConfigure(env, name, cfg):
	env.log("docker-compose configure %s" % name)
	enable = cfg.getboolean('systemd.enable', fallback = True)
	if enable:
		spath = cfg.get('path', fallback = '')
		if spath == '':
			raise env.error("docker-compose:%s path is empty" % name)
		tpldat = {
			'serviceName': name,
			'servicePath': spath,
		}
		systemd.configure(env, 'docker-compose', 'service', name, tpldat)
