#!/bin/sh -eu
docker run -it --rm \
	-e PYTHONPATH=/opt/src/sadm \
	-v ${PWD}/docker/bin:/opt/sadm/bin \
	-v ${PWD}/docker/etc:/etc/opt/sadm \
	-v ${PWD}:/opt/src/sadm sadmtest $@
exit 0
