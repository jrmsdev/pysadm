#!/usr/bin/env python3

# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

# https://packaging.python.org/guides/distributing-packages-using-setuptools/

from setuptools import setup, find_packages

def main():
	setup(
		setup_requires = ['setuptools_scm>=3.3'],
		use_scm_version = {'write_to': '_sadm/_version.py'},
		packages = find_packages(),
		py_modules = ['sadm'],
	)

if __name__ == '__main__':
	main()
