# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import HTTPError
from pytest import raises

from _sadm.listen.wapp import config
from _sadm.listen.webhook import repo

PROVIDERS = [
	'bitbucket',
	'testing',
]

def test_providers_list():
	assert sorted(repo._provider.keys()) == PROVIDERS

def test_noprovider():
	with raises(HTTPError) as exc:
		repo.WebhookRepo(config, 'noprov', 'testing')
	err = exc.value
	assert err.status_code == 400
	assert err.body == 'webhook invalid provider: noprov'

def test_norepo():
	with raises(HTTPError) as exc:
		repo.WebhookRepo(config, 'testing', 'norepo')
	err = exc.value
	assert err.status_code == 400
	assert err.body == 'webhook testing repo not found: norepo'
