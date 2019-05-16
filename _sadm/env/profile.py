# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log

class Profile(object):
	name = None

	def __init__(self, name):
		self.name = name
