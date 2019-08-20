# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.listen.wapp import wapp, config
from .repo import WebhookRepo

__all__ = ['push']

@wapp.route('/hook/<provider>/<name>/push')
def push(provider, name):
	repo = WebhookRepo(config, provider, name)
	return 'done'
