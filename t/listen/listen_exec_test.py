# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from unittest.mock import Mock

from _sadm.listen import exec as _exec

def test_get_url(listen_wapp):
	with listen_wapp() as wapp:
		req = wapp.request()
		assert req.url == 'http://127.0.0.1/'
		url = _exec._getURL(req)
		assert url == 'http://127.0.0.1:3666'
