# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log

__all__ = ['WebappUser']

class WebappUser(object):
	name = None

	def __init__(self, name, sess = None):
		self.name = name
		self.sess = sess
