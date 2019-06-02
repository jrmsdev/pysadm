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

RUN mkdir -p /opt/sadm/bin
COPY docker/bin /opt/sadm/bin

RUN mkdir -p /etc/opt/sadm
COPY docker/etc/deploy.cfg /etc/opt/sadm

WORKDIR /opt/src/sadm
