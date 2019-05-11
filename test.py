#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

from unittest import TestLoader

ldr = TestLoader()
suite = ldr.discover('.', '*_test.py')

if __name__ == '__main__':
    import sys
    from unittest import TextTestRunner

    verbose = 1
    if '-v' in sys.argv:
        verbose = 2

    rnr = TextTestRunner(verbosity=verbose)
    rst = rnr.run(suite)

    sys.exit(len(rst.errors))
