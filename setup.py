#!/usr/bin/env python3

# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

# https://packaging.python.org/guides/distributing-packages-using-setuptools/

from setuptools import setup, find_packages

def main():
	setup(
		python_requires = '~=3.4',
		setup_requires = ['setuptools_scm>=3.3'],
		use_scm_version = {'write_to': 'sadm/_version.py'},
		packages = find_packages(),
	)

if __name__ == '__main__':
	main()
