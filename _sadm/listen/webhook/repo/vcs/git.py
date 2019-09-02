# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import log
from _sadm.utils.vcs import git

__all__ = ['GitRepo']

class GitRepo(object):

	def hook(self, action, args):
		repodir = args.get('repo.path', 'NOREPOPATH')
		log.debug("hook action %s repo dir %s" % (action, repodir))
		if action == 'push':
			log.debug("git deploy %s" % repodir)
			git.deploy(repodir)
