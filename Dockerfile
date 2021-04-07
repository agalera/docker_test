FROM python:3.8-slim

ADD . /opt/
WORKDIR /opt
RUN python setup.py develop

CMD bash

