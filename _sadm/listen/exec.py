# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json
import sys
from urllib.parse import urlparse

from _sadm import log, libdir, version
from _sadm.listen.client import ListenClient
from _sadm.listen.webhook.repo.vcs.git import GitRepo
from _sadm.utils import sh, path
from _sadm.utils.cmd import callCheck

__all__ = ['dispatch', 'main']

#
# webhook dispatch task (exec new process)
#

def dispatch(req, task, action, taskArgs):
	log.debug("dispatch task: %s - action: %s" % (task, action))
	reqURL = urlparse(req.url)
	if reqURL.scheme == '':
		reqURL.scheme = 'http'
	obj = {
		'sadm.log': log.curLevel(),
		'sadm.listen.url': "%s://%s" % (reqURL.scheme, reqURL.netloc),
		'task': task,
		'task.action': action,
		'task.args': taskArgs,
	}
	taskfn = None
	with sh.mktmp(prefix = __name__, suffix = ".%s.json" % task) as fh:
		taskfn = fh.name()
		fh.write(json.dumps(obj))
	_sched(taskfn)

def _sched(taskfn):
	self = libdir.fpath('listen', 'exec.py')
	cmd = [sys.executable, self, taskfn]
	atcmd = "echo 'sleep 1 && %s' | at now" % ' '.join(cmd)
	log.debug("run: %s" % atcmd)
	callCheck(atcmd)

#
# task exec main (runs under a new process)
#

def main(args):
	if len(args) != 1:
		print('ERROR: sadm-listen exec invalid args', file = sys.stderr)
		return 1
	taskfn = args[0]
	obj = None
	try:
		with open(taskfn, 'r') as fh:
			obj = json.load(fh)
	finally:
		path.unlink(taskfn)
	log.init(obj.get('sadm.log', 'warn'))
	log.debug(version.string('sadm-listen'))
	log.debug("task file %s" % taskfn)
	task = obj.get('task', None)
	if task is None:
		raise RuntimeError('listen.exec task not set')
	taskAction = obj.get('task.action', None)
	if taskAction is None:
		raise RuntimeError("listen.exec task %s: no action" % task)
	taskArgs = obj.get('task.args', None)
	if taskArgs is None:
		raise RuntimeError("listen.exec task %s: no args" % task)
	cliURL = obj.get('sadm.listen.url', 'http://127.0.0.1:3666')
	cli = ListenClient(cliURL)
	cli.exec(task, taskAction, taskArgs)
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
