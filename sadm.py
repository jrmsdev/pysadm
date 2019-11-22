# coding: utf-8

# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from _sadm import version
from _sadm.cmd import build as build_cmd
from _sadm.cmd import deploy as deploy_cmd
from _sadm.cmd import host as host_cmd
from _sadm.cmd import setup as setup_cmd

__license__ = 'BSD'
__version__ = version.get()
__author__ = 'Jeremías Casteglione <jrmsdev@gmail.com>'

__all__ = ['build', 'deploy', 'setup']

build = build_cmd.main
deploy = deploy_cmd.main
host = host_cmd.main
setup = setup_cmd.main
