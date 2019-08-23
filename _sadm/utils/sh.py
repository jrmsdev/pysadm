# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import os
import os.path
import shutil as _sh
import tempfile

from contextlib import contextmanager

__all__ = ['TmpFile', 'makedirs', 'chmod', 'chown', 'mktmp', 'mktmpdir',
	'getcwd', 'chdir', 'getuid', 'getgid', 'lockd']

class TmpFile(object):
	_fd = None
	_fn = None
	_rm = None

	def __init__(self, suffix = None, prefix = None, dir = None, remove = False):
		if prefix is not None:
			if not prefix.endswith('.'):
				prefix = "%s." % prefix
		self._fd, self._fn = tempfile.mkstemp(suffix = suffix,
			prefix = prefix, dir = dir, text = False)
		self._rm = remove

	def __enter__(self):
		return self

	def __exit__(self, *args):
		self.close()
		if self._rm:
			self.unlink()

	def close(self):
		os.close(self._fd)

	def unlink(self):
		os.unlink(self._fn)

	def write(self, data):
		if isinstance(data, str):
			data = data.encode('utf-8')
		os.write(self._fd, data)

	def name(self):
		return self._fn

class _ShUtil(object):
	makedirs = os.makedirs
	chmod = os.chmod
	chown = _sh.chown
	mktmp = None
	mktmpdir = tempfile.mkdtemp
	getcwd = os.getcwd
	chdir = os.chdir
	getuid = os.getuid
	getgid = os.getgid
	lockd = None

	def __init__(self):
		self.mktmp = self._mktmp
		self.lockd = self._lockd

	def _mktmp(self, suffix = None, prefix = None, dir = None, remove = False):
		return TmpFile(suffix = suffix, prefix = prefix, dir = dir, remove = remove)

	def _lockd(path):
		fn = os.path.join(path, '.sadmlock')
		try:
			with open(fn, 'x') as fh:
				fh.write('1\n')
				fh.flush()
			yield
		finally:
			os.unlink(fn)

shutil = _ShUtil()

def makedirs(name, mode = 0o0755, exists_ok = False):
	return shutil.makedirs(name, mode = mode, exist_ok = exists_ok)

def chmod(path, mode):
	return shutil.chmod(path, mode)

def chown(path, user = None, group = None):
	return shutil.chown(path, user = user, group = group)

def mktmp(suffix = None, prefix = None, dir = None, remove = False):
	return shutil.mktmp(suffix = suffix, prefix = prefix, dir = dir, remove = remove)

def mktmpdir(suffix = None, prefix = None, dir = None):
	return shutil.mktmpdir(suffix = suffix, prefix = prefix, dir = dir)

def getcwd():
	return shutil.getcwd()

def chdir(path):
	return shutil.chdir(path)

def getuid():
	return shutil.getuid()

def getgid():
	return shutil.getgid()

@contextmanager
def lockd(path):
	try:
		yield shutil.lockd(path)
	finally:
		pass
