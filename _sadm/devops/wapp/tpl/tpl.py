# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import bottle

from datetime import datetime

from _sadm import version

__all__ = ['parse']

class Template(object):
	name = None
	__unset = object()

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

	@property
	def now(self):
		return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

	def __getitem__(self, name):
		return self.get(name)

	def get(self, name, default = __unset):
		val = self.data.get(name, None)
		if val is None:
			if default is self.__unset:
				raise KeyError("template %s: %s" % (self.name, name))
			else:
				return default
		return val

def parse(name, **data):
	return bottle.template(name, tpl = Template(name, data))
