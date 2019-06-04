# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.plugin.utils import cmd
from _sadm.plugin.utils.scripts import Scripts

__all__ = ['deploy']

scripts = Scripts('apache')

def deploy(env):
	_reload = False
	args = env.settings.getlist('apache', 'conf.disable')
	if len(args) > 0:
		_reload = True
		scripts.run('disconf.sh', args)
	args = env.settings.getlist('apache', 'mod.disable')
	if len(args) > 0:
		_reload = True
		scripts.run('dismod.sh', args)
	args = env.settings.getlist('apache', 'site.disable')
	if len(args) > 0:
		_reload = True
		scripts.run('dissite.sh', args)
	args = env.settings.getlist('apache', 'conf.enable')
	if len(args) > 0:
		_reload = True
		scripts.run('enconf.sh', args)
	args = env.settings.getlist('apache', 'mod.enable')
	if len(args) > 0:
		_reload = True
		scripts.run('enmod.sh', args)
	args = env.settings.getlist('apache', 'site.enable')
	if len(args) > 0:
		_reload = True
		scripts.run('ensite.sh', args)
	if _reload:
		scripts.run('reload.sh')
