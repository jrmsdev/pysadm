# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from os import path

def gen(env):
	env.log("%s.setup.artifact" % env.name())
	base = path.normpath(env.build.rootdir())
	fn = base + '.setup.artifact'
	with open(fn, 'x') as fh:
		fh.write('# testing\n')
	return fn
