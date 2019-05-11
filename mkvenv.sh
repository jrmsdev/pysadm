#!/bin/sh -eu

# Copyright (c) Jeremías Casteglione <jrmsdev@gmail.com>
# See LICENSE file.

ENVDIR=${1:-'/opt/venv/pysadm'}
PIP=${ENVDIR}/bin/pip

python3 -m venv --prompt sadm --clear ${ENVDIR}

${PIP} install -r requirements-venv.txt --upgrade
${PIP} list
