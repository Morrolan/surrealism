#!/usr/bin/env bash

apt-get update
apt-get install -y python2.7
apt-get install -y python3.5
apt-get install -y python-virtualenv
apt-get install -y git

mkdir /home/vagrant/surrealism27
cd /home/vagrant
virtualenv -p /usr/bin/python2.7 /home/vagrant/surrealism27
cd /home/vagrant/surrealism27
source /home/vagrant/surrealism27/bin/activate
sudo pip install nose
sudo pip install rednose
sudo pip install coveralls
deactivate


mkdir /home/vagrant/surrealism35
cd /home/vagrant
virtualenv -p /usr/bin/python3.5 /home/vagrant/surrealism35
cd /home/vagrant/surrealism35
source /home/vagrant/surrealism35/bin/activate
sudo pip install nose --upgrade
sudo pip install rednose --upgrade
sudo pip install coveralls --upgrade
deactivate