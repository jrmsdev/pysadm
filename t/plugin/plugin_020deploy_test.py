# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path, makedirs
from shutil import rmtree, move

def _build(pnew, pname, ns = '_sadm'):
	print('-- deploy build plugin:', pname)
	depdir = path.join('tdata', 'deploy', 'plugin', pname)
	targetdir = path.join('tdata', 'deploy.target', 'plugin', pname)
	for dirrm in (depdir, targetdir):
		if path.isdir(dirrm):
			rmtree(dirrm)
	p = pnew(pname, ns = ns, cfgfn = 'config-build.ini')
	p.build()
	makedirs(depdir, exist_ok = True)
	metadir = path.join('tdata', 'build', 'plugin', pname + '.meta')
	for fn in ('configure.ini', 'meta.json', pname + '.tar'):
		src = path.join(metadir, fn)
		dst = path.join(depdir, fn)
		move(src, dst)

def test_deploy_testing(testing_plugin):
	_build(testing_plugin, 'testing', ns = '_sadmtest')
	print('-- deploy plugin: testing')
	p = testing_plugin('testing', ns = '_sadmtest', deploy = True)
	p.deploy()

def test_all_deploy(testing_plugin):
	makedirs(path.join('tdata', 'deploy', 'plugin'), exist_ok = True)
	t = testing_plugin(deploy = True, ns = '_sadmtest')
	for opt in t._env.config.options('deploy'):
		if opt.startswith('env.'):
			pname = '.'.join(opt.split('.')[1:])
			if pname == 'testing':
				continue
			_build(testing_plugin, pname)
			print('-- deploy plugin:', pname)
			p = testing_plugin(pname, deploy = True)
			p.deploy()
