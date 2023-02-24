# install.py
# Version: 1.0.0
# Contains main processing code required for DaftPunk cosplay
# Author: Billy Wood

import os
import animationPlayer
import threading
from mouthAnims import runMouthAnims
from audioMonitor import runAudioMonitor
from animationPlayer import playAnimation, clearMatrix
from thingsboardTransmitter import ThingsBoardTransmitter

def runVoiceChanger():
    os.system("/usr/bin/play \"|rec --buffer 2096 -d synth sine fmod 5 echos 0.8 0.88 50 0.6\"")

def main():
    # Setup the Thingsboard transmitter
    thingsBoardTransmitter = ThingsBoardTransmitter()

    # Play animation on boot
    playAnimation("/home/pi/DaftPunkCosplay/pixelart animations/Hello.png", 100)
    clearMatrix()

    voiceChangerThread = threading.Thread(target = runVoiceChanger)
    voiceChangerThread.start()
    audioMonitorThread = threading.Thread(target = runAudioMonitor, args = [thingsBoardTransmitter])
    audioMonitorThread.start()
    mouthAnimsThread = threading.Thread(target = runMouthAnims, args = [thingsBoardTransmitter])
    mouthAnimsThread.start()

main()
