FROM python:3.6.3
RUN apt-get -y upgrade \
    && apt-get -y install python3-pytest

