# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import os
import tempfile

__all__ = ['TmpFile', 'new']

class TmpFile(object):
	_fh = None
	_fn = None
	_rm = None
	encoding = None

	def __init__(self, suffix = None, prefix = None, dir = None, remove = False,
		encoding = None):
		if prefix and not prefix.endswith('.'):
			prefix = "%s." % prefix
		self._fh = tempfile.NamedTemporaryFile(suffix = suffix, prefix = prefix,
			dir = dir, delete = remove, encoding = encoding)
		self._fn = self._fh.name
		self._rm = remove
		self.encoding = encoding or 'utf-8'

	def __enter__(self):
		return self

	def __exit__(self, *args):
		self.close()
		if self._rm:
			self.unlink()

	def close(self):
		self._fh.close()

	def unlink(self):
		os.unlink(self._fn)

	def write(self, data):
		if isinstance(data, str):
			data = data.encode(self.encoding)
		self._fh.write(data)

	def flush(self):
		self._fh.flush()

	def name(self):
		return self._fn

def new(**kwargs):
	return TmpFile(**kwargs)
