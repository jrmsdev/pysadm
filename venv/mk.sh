#!/bin/sh -eu

ENVDIR=${1:-'/opt/venv/pysadm'}
PIP=${ENVDIR}/bin/pip

python3 -m venv --prompt sadm --clear ${ENVDIR}

${PIP} install --upgrade -r requirements.txt
${PIP} install --upgrade .

${PIP} list
exit 0
