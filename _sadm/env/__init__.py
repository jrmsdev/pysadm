# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log
from _sadm.env.profile import Profile

class Env(object):
	name = None
	profile = None
	cfgfile = None

	def __init__(self, profile, name, cfgfile):
		self.name = name
		self.profile = Profile(profile)
		self.cfgfile = cfgfile
