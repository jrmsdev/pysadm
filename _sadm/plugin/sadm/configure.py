# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import version

def configure(env):
	env.debug(env.name())
	return {
		'version': version.get(),
	}
