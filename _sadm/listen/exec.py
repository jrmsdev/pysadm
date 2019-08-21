# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json
import sys

from _sadm import log, libdir, version
from _sadm.listen.webhook.repo.provider.bitbucket import BitbucketProvider
from _sadm.utils import sh, path
from _sadm.utils.cmd import callCheck

__all__ = ['dispatch', 'main']

#
# webhook dispatch task (exec new process)
#

def dispatch(task, action, kwargs):
	log.debug("dispatch task: %s - action: %s" % (task, action))
	obj = {
		'sadm.log': log.curLevel(),
		'task': task,
		'task.action': action,
		'task.args': kwargs,
	}
	taskfn = None
	with sh.mktmp(prefix = __name__, suffix = ".%s.json" % task) as fh:
		taskfn = fh.name()
		fh.write(json.dumps(obj))
	try:
		_run(taskfn)
	finally:
		path.unlink(taskfn)

def _run(taskfn):
	self = libdir.fpath('listen', 'exec.py')
	cmd = [sys.executable, self, taskfn]
	log.debug("run: %s" % cmd)
	callCheck(cmd)

#
# task exec main (runs under a new process)
#

_taskman = {
	'webhook.repo.bitbucket': BitbucketProvider(),
}

def main(args):
	if len(args) != 1:
		print('ERROR: sadm-listen exec invalid args', file = sys.stderr)
		return 1
	taskfn = args[0]
	obj = None
	with open(taskfn, 'r') as fh:
		obj = json.load(fh)
	log.init(obj.get('sadm.log', 'warn'))
	log.debug(version.string('sadm-listen'))
	log.debug("task file %s" % taskfn)
	task = obj.get('task', None)
	if task is None:
		raise RuntimeError('listen.exec task not set')
	taskman = _taskman.get(task, None)
	if taskman is None:
		raise RuntimeError("listen.exec task %s: no manager" % task)
	taskAction = obj.get('task.action', None)
	if taskAction is None:
		raise RuntimeError("listen.exec task %s: no action" % task)
	taskArgs = obj.get('task.args', None)
	if taskArgs is None:
		raise RuntimeError("listen.exec task %s: no args" % task)
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
