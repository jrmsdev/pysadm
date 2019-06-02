#!/bin/sh -eu
docker run -it --rm \
	-v ${PWD}/docker/bin:/opt/sadm/bin \
	-v ${PWD}/docker/etc:/etc/opt/sadm \
	-v ${PWD}:/opt/src/sadm sadm $@
exit 0
