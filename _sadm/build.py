# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import tarfile

from collections import deque
from os import path

from _sadm import asset
from _sadm.errors import BuildError

class Manager(asset.Manager):
	_tar = None
	_tarfn = None

	def create(self):
		self._tarfn = path.normpath(self.rootdir()) + '.tar'
		# python 3.4 does not support 'x:' open mode
		# self._tar = tarfile.open(self._tarfn, 'x:')
		if path.isfile(self._tarfn):
			raise BuildError("%s file exists" % self._tarfn)
		self._tar = tarfile.open(self._tarfn, 'w')

	def close(self):
		if self._tar is not None:
			self._tar.close()

	def addfile(self, name, user = 'root', group = '', mode = 0o0644):
		if group == '':
			group = user
		fi = self._tar.gettarinfo(name = path.join(self.rootdir(), name), arcname = name)
		fi.uid = 0
		fi.gid = 0
		fi.uname = user
		fi.gname = group
		fi.mode = mode
		self._tar.addfile(fi)
