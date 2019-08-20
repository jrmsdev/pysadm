#!/usr/bin/env python3

# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

import sys

from _sadm import listen
from _sadm.cmd import flags

def main():
	return listen.start()

if __name__ == '__main__':
	sys.exit(main())
