# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from _sadm import version

__all__ = ['parse']

class Template(object):
	name = None

	def __init__(self, name, data):
		self.name = name
		self.data = data
		self.data.update({
			'sadm': {
				'version': version.string('sadm'),
			}
		})

	@property
	def error(self):
		return self.data.get('error', None)

	def __getitem__(self, name):
		val = self.data.get(name, None)
		if val is None:
			raise KeyError("template %s: %s" % (self.name, name))
		return val

def parse(name, **data):
	return bottle.template(name, tpl = Template(name, data))
