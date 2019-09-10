# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.utils import path, systemd

__all__ = ['deploy']

_cfgfn = path.join(path.sep, 'etc', 'opt', 'sadm', 'listen.cfg')

def deploy(env):
	if path.isfile(_cfgfn):
		if systemd.status('sadm-listen', 'is-enabled') != 0:
			systemd.enable('sadm-listen')
		if systemd.status('sadm-listen') != 0:
			systemd.restart('sadm-listen')
