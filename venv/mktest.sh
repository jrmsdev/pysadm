#!/bin/sh -eu

ENVDIR=${1:-'/opt/venv/sadmtest'}
PIP=${ENVDIR}/bin/pip

python3 -m venv --prompt sadmtest --clear ${ENVDIR}

${PIP} install --upgrade -r venv/requirements-test.txt
${PIP} install --upgrade -r requirements.txt
${PIP} install --upgrade .

${PIP} list
exit 0
