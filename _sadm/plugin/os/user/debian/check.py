# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from collections import deque
from pwd import getpwuid

__all__ = ['check']

def check(env):
	diff = deque()
	for user in env.settings['os.user']:
		uid = env.settings.getint('os.user', user)
		try:
			info = getpwuid(uid)
		except KeyError:
			diff.append((user, uid))
			env.warn("%d %s not found" % (uid, user))
		else:
			env.log("%d %s OK" % (uid, user))
	return diff
