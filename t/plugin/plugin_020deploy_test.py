# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path, makedirs
from shutil import rmtree, move

def _build(pnew, pname):
	depdir = path.join('tdata', 'deploy', 'plugin', pname)
	if path.isdir(depdir):
		rmtree(depdir)
	p = pnew(pname, cfgfn = 'config-build.ini')
	p.build()
	makedirs(depdir, exist_ok = True)
	metadir = path.join('tdata', 'build', 'plugin', pname + '.meta')
	for fn in ('configure.ini', 'meta.json', pname + '.tar'):
		src = path.join(metadir, fn)
		dst = path.join(depdir, fn)
		move(src, dst)

def test_deploy_sync(testing_plugin):
	_build(testing_plugin, 'sync')
	p = testing_plugin('sync', deploy = True)
	p.deploy()
