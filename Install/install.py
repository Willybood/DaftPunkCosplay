# install.py
# Version: 1.0.0
# Installs dependences needed for Daft Punk cosplay
# Author: Billy Wood

import os
from shutil import copy2

def install_dependencies():
    print("================== Updating package lists ==================")
    os.system("sudo apt-get update")
    print("================== Updated package lists ==================")

    print("================== Start Installing PIP ==================")
    os.system("sudo apt install python3-pip -y")
    print("================== Completed Installing PIP ==================")

    print("================== Start Updating PIP ==================")
    os.system("sudo pip3 install --upgrade pip")
    print("================== Completed Updating PIP ==================")

    print("================== Start Installing Setuptools and Libatlas ==================")
    os.system("sudo apt install python-setuptools libatlas-base-dev -y")
    print("================== Completed Installing Setuptools and Libatlas ==================")

    print("================== Start Installing rpi_ws281x ==================")
    os.system("sudo pip3 install rpi_ws281x")
    print("================== Completed Installing rpi_ws281x ==================")
    
    print("================== Start Installing Sox ==================")
    os.system("sudo apt-get install sox -y")
    print("================== Completed Installing Sox ==================")
    
    print("================== Setup voice bonnet ==================")
    os.system("sudo apt-get install git -y")
    os.system("git clone https://github.com/HinTak/seeed-voicecard")
    os.system("cd seeed-voicecard")
    os.system("sudo ./install.sh")
    print("================== Completed setting up voice bonnet ==================")

    print("================== Rebooting ==================")
    os.system("sudo reboot")

install_dependencies()
