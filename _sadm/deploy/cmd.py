# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log, env, deploy

def run(envname, sumode):
	log.debug("run %s sumode=%s" % (envname, sumode))
	rc, _ = env.run('deploy', envname, 'deploy', cfgfile = deploy.cfgfile, sumode = sumode)
	return rc
