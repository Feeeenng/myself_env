#!/bin/bash

mkdir -p /opt/python3.6
apt-get -y install libbz2-dev libgdbm-dev liblzma-dev libreadline-dev libsqlite3-dev libssl-dev tcl-dev tk-dev dpkg-dev
wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz
tar xf Python-3.6.2.tgz
cd Python-3.6.2
./configure --prefix=/opt/python3.6 --enable-optimizations
make -j4 && make install
ln -s /opt/python3.6/bin/python3.6 /usr/bin/python3.
ln -s /opt/python3.6/bin/pip3.6 /usr/local/bin/pip3.6
