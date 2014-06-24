#!/usr/bin/env bash

cd /home/vagrant/surrealism27
source /home/vagrant/surrealism27/bin/activate
cd surrealism
sudo git checkout develop
sudo python setup.py register
sudo python setup.py build sdist bdist_egg upload
deactivate

cd /home/vagrant/surrealism32
source /home/vagrant/surrealism32/bin/activate
cd surrealism
sudo git checkout develop
sudo python setup.py build bdist_egg upload
deactivate