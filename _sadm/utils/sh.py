# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import os
import shutil as _sh

__all__ = ['makedirs']

class _ShUtil(object):
	makedirs = os.makedirs
	chmod = os.chmod
	chown = _sh.chown

shutil = _ShUtil()

def makedirs(name, mode = 0o0755, exists_ok = False):
	return shutil.makedirs(name, mode = mode, exist_ok = exists_ok)

def chmod(path, mode):
	return shutil.chmod(path, mode)

def chown(path, user = None, group = None):
	return shutil.chown(path, user = user, group = group)
