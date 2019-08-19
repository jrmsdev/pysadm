# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import _sadm.listen.webhook

from _sadm.listen.wapp import wapp

__all__ = ['start']

def start():
	return wapp.run()
