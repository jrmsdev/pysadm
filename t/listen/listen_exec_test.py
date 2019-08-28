# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

from _sadmtest import mock

from _sadm.listen import exec as _exec
from _sadm.listen import wapp

def test_get_url(listen_wapp):
	with mock.log():
		with listen_wapp() as wapp:
			req = wapp.request()
			assert req.url == 'http://127.0.0.1/'
			url = _exec._getURL(req)
			assert url == 'http://127.0.0.1:3666'

def test_main_no_args(listen_wapp):
	with mock.log():
		with mock.utils(None):
			with listen_wapp() as wapp:
				rc = _exec.main([])
				assert rc == 1

def test_main_no_task_file(listen_wapp):
	cfgfn = path.join('tdata', 'listen', 'exec', 'listen.cfg')
	cfg = wapp._newConfig(cfgfn)
	with mock.log():
		with mock.utils(cfg, tag = 'no_task_file'):
			with listen_wapp():
				rc = _exec.main(['no.task.file'])
				assert rc == 2

def test_main_no_task(listen_wapp):
	cfgfn = path.join('tdata', 'listen', 'exec', 'listen.cfg')
	cfg = wapp._newConfig(cfgfn)
	with mock.log():
		with mock.utils(cfg, tag = 'no_task'):
			with listen_wapp():
				rc = _exec.main(['tdata/listen/exec/unset.task'])
				assert rc == 3
