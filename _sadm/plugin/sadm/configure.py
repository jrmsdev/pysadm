# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import version

def configure(env, cfg):
	env.debug(env.name())
	s = env.settings2
	s.set('sadm', 'version', version.get())
