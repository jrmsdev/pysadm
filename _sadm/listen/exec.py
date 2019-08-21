# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import json

from _sadm import log
from _sadm.utils import sh, path

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
	log.debug("run: %s" % taskfn)
