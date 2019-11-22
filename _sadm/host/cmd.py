# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

__all__ = ['main', 'flags']

def flags(parser):
	pass

def main(env, args):
	env.debug("main %s" % env.name())
	return 0
