# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from bottle import request

from _sadm import log
from _sadm.listen.wapp import wapp
# ~ from _sadm.listen.webhook.repo.vcs.git import GitRepo

__all__ = ['exech']

# ~ _taskman = {
	# ~ 'webhook.repo.git': GitRepo(),
# ~ }

	# ~ taskman = _taskman.get(task, None)
	# ~ if taskman is None:
		# ~ raise RuntimeError("listen.exec task %s: no manager" % task)

	# ~ taskman.hook(taskAction, taskArgs)

@wapp.route('/_/exec/<task>/<action>', 'POST')
def exech(task, action):
	return 'OK\n'
