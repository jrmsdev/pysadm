# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

__all__ = ['parse']

class Template(object):
	name = None

	def __init__(self, name, data):
		self.name = name
		self.data = data

def parse(name, **data):
	return bottle.template(name, tpl = Template(name, data))
