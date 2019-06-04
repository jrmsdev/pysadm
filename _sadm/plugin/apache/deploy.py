# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.plugin.utils import cmd
from _sadm.plugin.utils.scripts import Scripts

__all__ = ['deploy']

scripts = Scripts('apache')

def deploy(env):
	scripts.run('dissite.sh', env.settings.getlist('apache', 'sites.disable'))
	scripts.run('ensite.sh', env.settings.getlist('apache', 'sites.enable'))
	scripts.run('reload.sh')
