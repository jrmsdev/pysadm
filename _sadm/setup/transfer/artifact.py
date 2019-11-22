#!/usr/bin/env python3

# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

# sadm.env setup
# https://pypi.org/project/sadm/

import sys

from os import path, getenv
from subprocess import call

def main():
	env = getenv('SADM_ENV', 'default')
	profile = getenv('SADM_PROFILE', 'default')
	rootdir = getenv('SADM_ROOTDIR', path.join(path.sep, 'opt', 'sadm'))
	return 0

if __name__ == '__main__':
	sys.exit(main()) # pragma: no cover
