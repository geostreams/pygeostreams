FROM ubuntu:16.04
MAINTAINER Rob Kooper <kooper@illinois.edu>

RUN apt-get -q -q update && apt-get install -y --no-install-recommends \
        netcat \
        python \
        python-pip \
    && pip install --upgrade setuptools \
    && rm -rf /var/lib/apt/lists/* \
    && adduser --system clowder

COPY pygeotemporal /tmp/pygeotemporal/pygeotemporal
COPY setup.py requirements.txt /tmp/pygeotemporal/

RUN pip install --upgrade  -r /tmp/pygeotemporal/requirements.txt \
    && pip install --upgrade /tmp/pygeotemporal \
    && rm -rf /tmp/pygeotemporal
