# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.utils import path, systemd

__all__ = ['deploy']

_cfgfn = path.join(path.sep, 'etc', 'opt', 'sadm', 'listen.cfg')

def deploy(env):
	if path.isfile(_cfgfn):
		rc = systemd.status('sadm-listen')
		if rc != 0:
			systemd.enable('sadm-listen')
			systemd.start('sadm-listen')
