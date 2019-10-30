# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from string import Template

from _sadm.errors import PluginError
from _sadm.utils import builddir

__all__ = ['build']

def build(env):
	for args in env.session.get('templates.build', []):
		name = args[0]
		src = args[1]
		dst = args[2]
		opts = args[3]
		_parse(env, name, src, dst, opts)

def _parse(env, name, src, dst, args):
	env.log("parse %s: src=%s dst=%s" % (name, src, dst))
	with env.assets.open(src) as srcfh:
		tpl = Template(srcfh.read())
		with builddir.create(env, dst) as dstfh:
			try:
				dstfh.write(tpl.substitute(args))
			except KeyError as err:
				raise PluginError("template %s key error: %s" % (name, err))
