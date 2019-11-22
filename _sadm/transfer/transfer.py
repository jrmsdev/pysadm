# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.errors import BuildError
from _sadm.transfer.artifact import deploy, setup

__all__ = ['cargo', 'artifact']

def cargo(env, artifact):
	env.debug("cargo %s" % artifact)
	if artifact == 'deploy':
		return deploy.cargo(env)
	elif artifact == 'setup':
		return setup.cargo(env)
	raise BuildError("unknown artifact: %s" % artifact)

def artifact(env, name):
	env.debug("artifact %s" % name)
	if name == 'deploy':
		return deploy.artifact(env)
	elif name == 'setup':
		return setup.artifact(env)
	raise BuildError("unknown artifact: %s" % name)
