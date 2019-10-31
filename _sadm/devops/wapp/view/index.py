# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm.devops.wapp.tpl import tpl

__all__ = ['handle']

def handle():
	return tpl.parse('index.html')
