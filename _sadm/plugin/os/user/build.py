# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.plugin.utils import builddir

__all__ = ['build']

def build(env):
	homedir = env.settings.get('os', 'home.dir')
	env.debug("os home dir %s" % homedir)
	for user in env.settings['os.user']:
		uid = env.settings.getint('os.user', user)
		env.log("%d %s" % (uid, user))
		_sshauth(env, user)

def _sshauth(env, user):
	pass
