# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path, makedirs
from shutil import rmtree, move

def _build(pnew, pname):
	depdir = path.join('tdata', 'deploy', 'plugin', pname)
	targetdir = path.join('tdata', 'deploy.target', 'plugin', pname)
	for dirrm in (depdir, targetdir):
		if path.isdir(dirrm):
			rmtree(dirrm)
	p = pnew(pname, cfgfn = 'config-build.ini')
	p.build()
	makedirs(depdir, exist_ok = True)
	metadir = path.join('tdata', 'build', 'plugin', pname + '.meta')
	for fn in ('configure.ini', 'meta.json', pname + '.tar'):
		src = path.join(metadir, fn)
		dst = path.join(depdir, fn)
		move(src, dst)

def test_all_deploy(testing_plugin):
	makedirs(path.join('tdata', 'deploy', 'plugin'), exist_ok = True)
	t = testing_plugin(deploy = True, ns = '_sadmtest')
	for opt in t._env.config.options('deploy'):
		if opt.startswith('env.'):
			env = '.'.join(opt.split('.')[1:])
			if env == 'testing':
				continue
			_build(testing_plugin, env)
			p = testing_plugin(env, deploy = True)
			p.deploy()
