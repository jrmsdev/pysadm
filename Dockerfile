FROM debian:buster-slim

LABEL maintainer="Jeremías Casteglione <jrmsdev@gmail.com>"
LABEL version="19.7.26"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get clean
RUN apt-get update

RUN apt-get dist-upgrade -y --purge
RUN apt-get install -y --no-install-recommends sudo python3 python3-pip

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

RUN rm -rf /root/.cache
RUN rm -f /tmp/requirements.txt

RUN apt-get clean
RUN apt-get autoremove -y --purge

RUN rm -rf /var/lib/apt/lists/*
RUN rm -f /var/cache/apt/archives/*.deb
RUN rm -f /var/cache/apt/*cache.bin

RUN mkdir -p /opt/sadm
RUN mkdir -p /etc/opt/sadm

ARG SADM_UID=1000
ARG SADM_GID=1000

RUN groupadd -g ${SADM_GID} sadm
RUN useradd -c sadm -m -d /home/sadm -s /bin/bash -g ${SADM_GID} -u ${SADM_UID} sadm

RUN chgrp sadm /opt/sadm
RUN chmod g+w /opt/sadm

COPY etc/sudoers.d/sadm /etc/sudoers.d
RUN chmod 440 /etc/sudoers.d/sadm

USER sadm:sadm
WORKDIR /opt/src/sadm

CMD /bin/bash -i -l
