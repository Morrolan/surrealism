#!/usr/bin/env bash

apt-get update
apt-get install -y python2.7
apt-get install -y python3.2
apt-get install -y python-virtualenv
apt-get install -y git

mkdir /home/vagrant/surrealism27
cd /home/vagrant
virtualenv -p /usr/bin/python2.7 /home/vagrant/surrealism27
cd /home/vagrant/surrealism27
source /home/vagrant/surrealism27/bin/activate
pip install nose
pip install rednose
deactivate


mkdir /home/vagrant/surrealism32
cd /home/vagrant
virtualenv -p /usr/bin/python3.2 /home/vagrant/surrealism32
cd /home/vagrant/surrealism32
source /home/vagrant/surrealism32/bin/activate
pip install nose
pip install rednose
deactivate