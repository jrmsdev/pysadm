# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import route, view

from _sadm import log
from _sadm import _cfg as cfg
from _sadm.web import tpl

@route('/profile')
@view('profile.html')
@tpl.data('profile')
def index():
	log.debug('index')
	config = cfg.new()
	return {
		'profiles': _getallProfiles(config),
	}

def _getallProfiles(config):
	l = []
	for p in config.listProfiles():
		l.append(_getProfile(config, p))
	return l

def _getProfile(config, p):
	return {
		'name': p,
		'envs': config.listEnvs(p),
	}
