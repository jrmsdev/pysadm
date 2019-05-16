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
		# ~ 'profiles': _getallProfiles(config),
		'profiles': [],
	}

def _getallProfiles(config):
	d = {}
	for s in config.sections():
		log.debug("section %s" % s)
		if s.startswith('profile.'):
			p = '.'.join(s.split('.')[1:])
			d[p] = _getProfile(config, p)
	l = []
	for n in sorted(d.keys()):
		l.append(d[n])
	return l

def _getProfile(config, p):
	return {
		'name': p,
		'envs': _getProfileEnvs(config, p),
	}

def _getProfileEnvs(config, p):
	e = {}
	for n in config.options("profile.%s" % p):
		log.debug("option %s" % n)
		if n.startswith('env.'):
			env = '.'.join(n.split('.')[1:])
			e[env] = True
	return sorted(e.keys())
