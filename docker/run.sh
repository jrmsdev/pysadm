#!/bin/sh -eu
docker run -it --rm -v ${PWD}:/opt/src/sadm sadm $@
exit 0
