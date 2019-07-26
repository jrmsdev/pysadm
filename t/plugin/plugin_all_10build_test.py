# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from _sadm.configure import pluginsList

_srcdir = path.dirname(path.dirname(path.dirname(__file__)))

def test_build_testing(testing_plugin):
	p = testing_plugin('testing', ns = '_sadmtest', cfgfn = 'config-build.ini')
	p.build()
	p.check.builddir.file('sadm.testing') # just to check it works both ways
	p.check.builddir.file('sadm.testing', 'testing\n')

def test_all_build(testing_plugin):
	for n in pluginsList():
		if n == 'testing':
			continue
		fn = path.join(_srcdir, 'tdata', 'plugin', n, 'config-build.ini')
		if path.isfile(fn):
			p = testing_plugin(n, cfgfn = 'config-build.ini')
			p.build()
			# check assets/testing.txt was sync'ed
			# so, all build tests should do that, yes...
			p.check.builddir.file('testing.txt', 'testing\n')
