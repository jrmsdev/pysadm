# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

__all__ = ['parse']

class Template(object):
	name = None

	def __init__(self, name, data):
		self.name = name
		self.data = data

	@property
	def error(self):
		return self.data.get('error', None)

def parse(name, **data):
	return bottle.template(name, tpl = Template(name, data))
