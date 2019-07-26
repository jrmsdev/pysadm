# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

# ~ from _sadm.configure import pluginsList

def test_build_testing(testing_plugin):
	p = testing_plugin('testing', ns = '_sadmtest', cfgfn = 'config-build.ini')
	p.build()
	p.check.builddir.file('sadm.testing', 'testing\n')

# ~ def test_all_configure(testing_plugin):
	# ~ for n in pluginsList():
		# ~ if n in ('testing', 'sadm', 'sadmenv'):
			# ~ continue
		# ~ p = testing_plugin(n)
		# ~ assert p.configure(), "%s plugin.configure failed" % n
