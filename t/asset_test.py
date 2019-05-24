# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from io import UnsupportedOperation
from os import path, makedirs, unlink
from pytest import raises
from shutil import rmtree

from _sadm.asset import Manager
from _sadm.errors import AssetError, AssetNotFoundError

_rootdir = path.join('tdata', 'testing')

def test_manager():
	m = Manager(_rootdir)
	assert m.rootdir().endswith(_rootdir)
	with m.open('asset.test') as fh:
		fh.close()
	with raises(AssetNotFoundError):
		m.open('nofile')

def test_asset_path():
	rdir = path.realpath(_rootdir)
	m = Manager(_rootdir)
	assert m.path('p0', 'p1', 'p2') == path.join(rdir, 'p0', 'p1', 'p2')
	assert m.path(path.sep, 'p0', 'p1', 'p2') == path.join(rdir, 'p0', 'p1', 'p2')

def test_read_only():
	rdir = path.join('tdata', 'tmp')
	fn = path.join(rdir, 'asset-readonly.test')
	if path.isfile(fn):
		unlink(fn)
	makedirs(rdir, exist_ok = True)
	with open(fn, 'x') as fh:
		fh.write('testing')
	assert path.isfile(fn)
	m = Manager(rdir)
	with raises(UnsupportedOperation, match = 'not writable'):
		with m.open('asset-readonly.test') as fh:
			fh.write('testing')
	unlink(fn)

def test_oserror():
	rdir = path.join('tdata', 'tmp')
	fn = path.join(rdir, 'asset-oserror.dir')
	if path.isdir(fn):
		rmtree(fn)
	makedirs(fn)
	assert path.isdir(fn)
	m = Manager(rdir)
	with raises(AssetError, match = ' Is a directory: '):
		m.open('asset-oserror.dir')
	rmtree(fn)
