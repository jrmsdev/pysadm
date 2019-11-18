# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.errors import BuildError
from _sadm.transfer.artifact import deploy

__all__ = ['cargo']

def cargo(env, artifact):
	env.debug("cargo %s" % artifact)
	if artifact == 'deploy':
		return deploy.cargo(env)
	raise BuildError("unknown artifact: %s" % artifact)
