# install.py
# Version: 1.0.0
# Installs dependences needed for Daft Punk cosplay
# Author: Billy Wood

import os
from shutil import copy2

def install_dependencies():
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
    
    print("================== Start Installing PyPNG ==================")
    os.system("sudo pip3 install git+https://gitlab.com/drj11/pypng@pypng-0.20220715.0")
    print("================== Completed Installing PyPNG ==================")

def edit_alsa_conf():
    print("================== Creating backup of alsa.conf ==================")
    copy2('/usr/share/alsa/alsa.conf', '/usr/share/alsa/alsa.conf.bak')
    print("================== Completed backup of alsa.conf -> alsa.conf.bak ==================")

    print("================== Replacing text in alsa.conf ==================")
    with open('/usr/share/alsa/alsa.conf', 'r') as file:
        filedata = file.read()
        filedata = filedata.replace("defaults.ctl.card 0", "defaults.ctl.card 1")
        filedata = filedata.replace("defaults.pcm.card 0", "defaults.pcm.card 1")
    with open('/usr/share/alsa/alsa.conf', 'w') as file:
        file.write(filedata)

    print("================== Completed replacing text in alsa.conf ==================")

install_dependencies()
edit_alsa_conf()
