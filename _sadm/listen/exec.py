# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json
import sys

from _sadm import log, libdir
from _sadm.utils import sh, path
from _sadm.utils.cmd import callCheck

__all__ = ['dispatch']

def dispatch(task, **kwargs):
	log.debug("dispatch task: %s" % task)
	taskfn = None
	with sh.mktmp(prefix = __name__, suffix = ".%s.json" % task) as fh:
		taskfn = fh.name()
		fh.write(json.dumps({'task': task, 'args': kwargs}))
	try:
		_run(taskfn)
	finally:
		path.unlink(taskfn)

def _run(taskfn):
	self = libdir.fpath('listen', 'exec.py')
	cmd = [sys.executable, self, taskfn]
	log.debug("run: %s" % cmd)
	callCheck(cmd)

def main(args):
	if len(args) != 1:
		print('ERROR: sadm-listen exec no args', file = sys.stderr)
		return 1
	taskfn = args[0]
	print(taskfn)
	task = None
	with open(taskfn, 'r') as fh:
		task = json.load(fh)
	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
