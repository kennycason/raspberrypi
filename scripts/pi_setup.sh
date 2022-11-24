#!/bin/sh

# general update
sudo apt update
sudo apt upgrade

# zsh + ohmyzsh
sudo apt install zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

sudo apt install vim
sudo apt install libpigpio-dev
pip install RPi.GPIO

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

# NRF24 Wireless Transmitter/Receiver
# https://github.com/bjarne-hansen/py-nrf24
sudo apt-get install pigpio python-pigpio python3-pigpio
pip install nrf24

#sudo apt-get install python-pip python-dev
#pip install RPi.GPIO
#pip install wiringPi
#pip install gpio