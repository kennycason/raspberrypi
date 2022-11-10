#!/bin/sh

# general update
sudo apt update
sudo apt upgrade

# zsh + ohmyzsh
sudo apt install zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

sudo apt install vim
sudo apt install libpigpio-dev

# python/opencv
pip install -U numpy
pip install opencv-python
sudo apt-get install libjasper-dev
sudo apt-get install libatlas-base-dev

# picamera 2
sudo apt install -y python3-pyqt5 python3-opengl
sudo apt install -y python3-picamera2

# astropi
sudo apt-get install sense-hat

#sudo apt-get install python-pip python-dev
#sudo pip install RPi.GPIO
#sudo pip install wiringPi
#sudo pip install gpio