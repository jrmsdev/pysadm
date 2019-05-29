# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.env.settings import Settings

__all__ = ['configure']

def configure(env, cfg):
	udir = cfg.get('os', 'users.config.dir', fallback = None)
	if udir is None:
		udir = env.settings.get('os', 'users.config.dir')

	fn = cfg.get('os', 'users.config.file', fallback = None)
	if fn is None:
		fn = env.settings.get('os', 'users.config.file')

	env.session.set('os.users.config.dir', udir)

	db = Settings()
	with env.assets.open(udir, fn) as fh:
		env.debug("users config %s" % fh.name)
		db.read_file(fh)

	_addusers(env, db, cfg)

def _addusers(env, db, cfg):
	l = cfg.getlist('os.user', 'add', fallback = [])
	for user in l:
		uid = db['users'][user]
		env.debug("add user %d %s" % (int(uid), user))
		env.settings['os.user'][user] = uid
		env.settings.add_section("os.user.%s" % user)
		for opt, val in db["user.%s" % user].items():
			env.settings["os.user.%s" % user][opt] = val
