# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__all__ = ['exec']

def exec(env, filename):
	env.debug("exec %s" % filename)
	env.start('host.exec')
	env.log(filename)
	env.end('host.exec')
