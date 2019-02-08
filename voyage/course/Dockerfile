# --------------------------------------------------------------
#
#   This file is part of voyage.
#    __file__ : DockerFile
#   __author__ = 'Sri Pandi, Satheesh Rathinakumar'
#
# --------------------------------------------------------------


FROM python:3.6-onbuild
#FROM python:3.6-slim

MAINTAINER Satheesh Rathinakumar <satheesh.rl@gmail.com>


ENV PYTHONDONTWRITEBYTECODE=True
ENV INSTALL_PATH /course

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --no-install-recommends libsasl2-dev python-dev \
  libldap2-dev libssl-dev vim python-matplotlib

RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

RUN pwd
RUN pip3 install --upgrade pip
COPY . .

RUN ls

ADD ./requirements.txt $INSTALL_PATH
RUN pip install -r requirements.txt

ADD . $INSTALL_PATH


