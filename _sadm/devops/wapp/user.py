# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__all__ = ['WebappUser', 'UserAuthError']

class UserAuthError(Exception):
	pass

class WebappUser(object):
	name = None

	def __init__(self):
		pass

	def auth(self, request):
		pass
