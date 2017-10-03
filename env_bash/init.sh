#!/bin/bash

mkdir -p /opt/python
apt-get -y install libbz2-dev libgdbm-dev liblzma-dev libreadline-dev libsqlite3-dev libssl-dev tcl-dev tk-dev dpkg-dev
wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz
tar xf Python-3.6.2.tgz
cd Python-3.6.2
./configure --prefix=/opt/python3.6 --enable-optimizations
make -j2 && make install
source /etc/profile
