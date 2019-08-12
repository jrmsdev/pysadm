# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path, unlink

from _sadm.utils import systemd

__all__ = ['deploy']

def deploy(env):
	destdir = env.settings.get('network.fail2ban', 'jail.destdir')
	jdisable = env.settings.getlist('network.fail2ban', 'jail.disable')
	for jn in jdisable:
		fn = path.join(destdir, jn + '.conf')
		if path.isfile(fn):
			env.log("remove %s" % fn)
			unlink(fn)
	systemd.restart('fail2ban')
	systemd.status('fail2ban')
