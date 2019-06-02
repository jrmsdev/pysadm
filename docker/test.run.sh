#!/bin/sh -eu
docker run -it --rm \
	-e PYTHONPATH=/opt/src/sadm \
	-v ${PWD}:/opt/src/sadm sadmtest $@
exit 0

	#~ -v ${PWD}/docker/bin:/opt/sadm/bin \
	#~ -v ${PWD}/docker/etc:/etc/opt/sadm \
