# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

def test_deploy_testing(testing_plugin):
	p = testing_plugin('testing', ns = '_sadmtest', deploy = True)
	p.deploy()

def test_deploy_sync(testing_plugin):
	p = testing_plugin('sync', deploy = True)
	p.deploy()
