#!/bin/sh -eu

ENVDIR=${1:-'/opt/venv/pysadmtest'}
PIP=${ENVDIR}/bin/pip

python3 -m venv --prompt sadmtest --clear ${ENVDIR}

${PIP} install -r venv/requirements-test.txt --upgrade
${PIP} install -r requirements.txt --upgrade
${PIP} install -e .

${PIP} list
exit 0