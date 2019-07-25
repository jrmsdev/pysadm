#!/bin/sh -eu

ENVDIR=${1:-'/opt/venv/pysadmdev'}
PIP=${ENVDIR}/bin/pip

python3 -m venv --prompt sadmdev --clear ${ENVDIR}

${PIP} install --upgrade -r venv/requirements-test.txt
${PIP} install --upgrade -r venv/requirements-dev.txt
${PIP} install --upgrade -r requirements.txt
${PIP} install --upgrade -e .

${PIP} list
exit 0
