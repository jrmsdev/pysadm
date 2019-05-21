# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path, makedirs

def build(env):
	env.debug('build')
	_setHostname(env)

def _setHostname(env):
	builddir = env.session.get('builddir')
	env.debug("builddir %s" % builddir)
	hostname = env.settings.get('os', 'hostname')
	hostfn = env.settings.get('os', 'hostname.file')
	if hostfn.startswith(path.sep):
		hostfn = hostfn.replace(path.sep, '', 1)
	fn = path.join(builddir, hostfn)
	env.debug("hostname file %s" % fn)
	mode = 'w'
	if not path.isfile(fn):
		mode = 'x'
	dstdir = path.dirname(fn)
	makedirs(dstdir, exist_ok = True)
	with open(fn, mode) as fh:
		fh.write(hostname.strip())
		fh.write('\n')
		fh.flush()
	env.log("%s %s" % (hostfn, hostname))
