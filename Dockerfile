FROM debian:stable-slim

LABEL maintainer="Jeremías Casteglione <jrmsdev@gmail.com>"
LABEL version="0.1"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get clean
RUN apt-get update

RUN apt-get dist-upgrade -y --purge
RUN apt-get install -y --no-install-recommends python3 python3-bottle

RUN apt-get clean
RUN apt-get autoremove -y --purge

RUN rm -rf /var/lib/apt/lists/*
RUN rm -f /var/cache/apt/archives/*.deb
RUN rm -f /var/cache/apt/*cache.bin

RUN mkdir -p /opt/sadm
RUN mkdir -p /etc/opt/sadm

#COPY docker/etc /etc/opt/sadm
#RUN find /etc/opt/sadm -type d -exec chmod 555 {} \;
#RUN find /etc/opt/sadm -type f -exec chmod 444 {} \;

#RUN mkdir -p /opt/sadm/bin
#COPY docker/bin /opt/sadm/bin
#RUN chmod 555 /opt/sadm/bin/*

RUN useradd -c sadm -m -s /bin/bash -U sadm

RUN chgrp sadm /opt/sadm
RUN chmod g+w /opt/sadm

USER sadm:sadm

WORKDIR /opt/src/sadm
