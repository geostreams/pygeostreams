FROM ubuntu:16.04
MAINTAINER Rob Kooper <kooper@illinois.edu>

RUN apt-get -q -q update && apt-get install -y --no-install-recommends \
        netcat \
        python \
        python-pip \
    && pip install --upgrade setuptools \
    && rm -rf /var/lib/apt/lists/* \
    && adduser --system clowder

COPY pygeostreams /tmp/pygeostreams/pygeostreams
COPY setup.py requirements.txt /tmp/pygeostreams/

RUN pip install --upgrade  -r /tmp/pygeostreams/requirements.txt \
    && pip install --upgrade /tmp/pygeostreams \
    && rm -rf /tmp/pygeostreams
