# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path
from subprocess import call

from _sadm import cfg

prun = path.join('.', 'docker', 'prun.py')

def test_devel_envs():
	config = cfg.new(cfgfile = path.join('docker', 'sadm.cfg'))
	for env in config.listEnvs('devel'):
		rc = call([prun, env])
		assert rc == 0, "%s %s failed: %d" % (prun, env, rc)
