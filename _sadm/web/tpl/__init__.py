# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from datetime import datetime
from _sadm import log, version

def data(view):
	def wrapper(func):
		def decorator(*args, **kwargs):
			_start = datetime.timestamp(datetime.now())
			log.debug("view data %s" % view)
			rst = func(*args, **kwargs)
			rst['view'] = view
			rst['version'] = version.get()
			rst['now'] = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
			rst['took'] = "%.5f" % (datetime.timestamp(datetime.now()) - _start)
			return rst
		return decorator
	return wrapper
