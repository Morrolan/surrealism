#!/usr/bin/env bash

cd /home/vagrant/surrealism27
source /home/vagrant/surrealism27/bin/activate
sudo mkdir surrealism
sudo git clone https://github.com/Morrolan/surrealism.git
sudo nosetests --rednose --with-xunit --xunit-file=/vagrant/results/nosetests2.7.xml /home/vagrant/surrealism27/surrealism/test_surrealism.py
/home/vagrant/surrealism27/bin/deactivate

cd /home/vagrant/surrealism32
source /home/vagrant/surrealism32/bin/activate
sudo mkdir surrealism
sudo git clone https://github.com/Morrolan/surrealism.git
cd surrealism
sudo nosetests --rednose --with-xunit --xunit-file=/vagrant/results/nosetests3.2.xml /home/vagrant/surrealism32/surrealism/test_surrealism.py
/home/vagrant/surrealism32/bin/deactivate