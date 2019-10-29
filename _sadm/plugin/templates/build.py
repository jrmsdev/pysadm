# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from string import Template

from _sadm.utils import builddir

__all__ = ['build']

def build(env):
	for args in env.session.get('templates.build', []):
		name = args[0]
		src = args[1]
		dst = args[2]
		_parse(env, name, src, dst)

def _parse(env, name, src, dst):
	env.log("parse %s: src=%s dst=%s" % (name, src, dst))
	with env.assets.open(src) as srcfh:
		tpl = Template(srcfh.read())
		with builddir.create(env, dst) as dstfh:
			dstfh.write(tpl.substitute({'tdata': 'testing'}))
