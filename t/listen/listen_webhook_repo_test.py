# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import HTTPError
from pytest import raises

from _sadm.listen.webhook import repo
from _sadm.listen.webhook.handlers import repo as repohdlr

PROVIDERS = [
	'bitbucket',
	'testing',
]

def test_providers_list():
	assert sorted(repo._provider.keys()) == PROVIDERS

def test_noprovider():
	with raises(HTTPError) as exc:
		repohdlr('noprovider', 'norepo', 'push')
	err = exc.value
	assert err.status_code == 400
	assert err.body == 'webhook invalid provider: noprovider'

def test_norepo():
	with raises(HTTPError) as exc:
		repohdlr('testing', 'norepo', 'push')
	err = exc.value
	assert err.status_code == 400
	assert err.body == 'webhook testing repo not found: norepo'
