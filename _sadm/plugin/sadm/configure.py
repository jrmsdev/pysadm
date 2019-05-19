# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import version

def configure(env, data):
	return {
		'version': version.get(),
	}
