# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log

def template(name):
	def wrapper(func):
		def decorator(*args, **kwargs):
			log.debug("template %s" % name)
			rst = func(*args, **kwargs)
			return rst
		return decorator
	return wrapper
