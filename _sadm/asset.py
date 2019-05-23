# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

class Manager(object):
	_dir = None

	def __init__(self, rootdir):
		self._dir = path.realpath(path.normpath(rootdir))

	def rootdir(self):
		return self._dir

	def path(self, name, *parts):
		relname = path.normpath(path.join(name, *parts))
		if relname.startswith(path.sep):
			relname.replace(path.sep, '', 1)
		return path.join(self._dir, relname)

	# TODO: catch os errors
	def open(self, name, *parts):
		return open(self.path(name, *parts), 'r')
