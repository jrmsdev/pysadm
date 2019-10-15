# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.web.view import about

def test_about(testing_webapp):
	wapp = testing_webapp('app')
	with wapp.mock() as ctx:
		d = about.about()
		print('D:', d)
		assert sorted(d.keys()) == [
			'bottleVersion',
			'curyear',
			'now',
			'pythonVersion',
			'sqliteLibVersion',
			'sqliteVersion',
			'took',
			'version',
			'view',
		]
		ctx.wapp.route.assert_called_once_with()
