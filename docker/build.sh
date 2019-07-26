#!/usr/bin/env bash
set -eu
TAG=${1:-''}
IMAGE='jrmsdev/sadm'
DOCKERFN='Dockerfile'
if test "X${TAG}" != "X"; then
	IMAGE="jrmsdev/sadm:${TAG}"
	DOCKERFN="Dockerfile.${TAG}"
fi
docker build -t ${IMAGE} -f ${DOCKERFN} .
exit 0
