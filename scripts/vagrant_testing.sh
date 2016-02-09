#!/usr/bin/env bash

cd /home/vagrant/surrealism27
source /home/vagrant/surrealism27/bin/activate
sudo mkdir surrealism
sudo git clone https://github.com/Morrolan/surrealism.git
cd surrealism
sudo git checkout master
sudo nosetests --rednose --with-xunit --xunit-file=/vagrant/results/nosetests2.7.xml /home/vagrant/surrealism27/surrealism/test_surrealism.py
python /home/vagrant/surrealism27/surrealism/large_output_test.py
deactivate

cd /home/vagrant/surrealism35
source /home/vagrant/surrealism35/bin/activate
sudo mkdir surrealism
sudo git clone https://github.com/Morrolan/surrealism.git
cd surrealism
sudo git checkout master
sudo nosetests --rednose --with-xunit --xunit-file=/vagrant/results/nosetests3.5.xml /home/vagrant/surrealism32/surrealism/test_surrealism.py
python /home/vagrant/surrealism35/surrealism/large_output_test.py
deactivate