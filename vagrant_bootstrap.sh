#!/usr/bin/env bash

apt-get update
apt-get install -y python2.7
apt-get install -y python3.2
apt-get install -y python-virtualenv

mkdir /home/vagrant/surrealism27
cd /home/vagrant
virtualenv -p /usr/bin/python2.7 /home/vagrant/surrealism27
cd /home/vagrant/surrealism27
source /home/vagrant/surrealism27/bin/activate
pip install nose
pip install rednose


mkdir /home/vagrant/surrealism32