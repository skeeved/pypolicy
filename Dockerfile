FROM python:3.6.3
RUN apt-get -y upgrade \
    && pip install pytest

