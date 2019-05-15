# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import route, view
from _sadm import log
from _sadm.web import tpl, syslog

@route('/syslog')
@view('syslog.html')
@tpl.data('syslog')
def index():
	limit = 100
	log.debug("last %d messages" % limit)
	lvlmap = dict()
	for lname, lid in syslog._LVLMAP.items():
		lvlmap[lid] = lname
	log.debug("lvlmap: %s" % lvlmap)
	return {
		'limit': limit,
		'msgs': syslog.last(limit),
		'lvlmap': lvlmap,
	}
