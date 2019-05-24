# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import tarfile

from collections import deque
from os import path

from _sadm import asset

class Manager(asset.Manager):
	_tar = None
	_tarfn = None

	def create(self):
		self._tarfn = path.normpath(self.rootdir()) + '.tar'
		self._tar = tarfile.open(self._tarfn, 'x:')

	def close(self):
		self._tar.close()

	def addfile(self, name, user = 'root', group = ''):
		if group == '':
			group = user
		self._tar.add(path.join(self.rootdir(), name), arcname = name)
