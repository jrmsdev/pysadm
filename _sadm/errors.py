# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

class Error(Exception):
	typ = None
	msg = None

	def __init__(self, typ, msg):
		self.typ = typ
		self.msg = msg

	def __str__(self):
		return "%s: %s" % (self.typ, self.msg)

	def __repr__(self):
		return "<sadm.%s: %s>" % (self.typ, self.msg)

	def __eq__(self, err):
		return self.typ == err.typ and self.msg == err.msg

ProfileError = lambda msg: Error('ProfileError', msg)
EnvError = lambda msg: Error('EnvError', msg)
