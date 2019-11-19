# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.transfer import extractor

__all__ = ['gen']

def gen(env):
	return extractor.gen(env, 'deploy')
