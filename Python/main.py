# install.py
# Version: 1.0.0
# Contains main processing code required for Stormtrooper cosplay
# Author: Billy Wood

import os
import threading
from audioMonitor import runAudioMonitor

def runVoiceChanger():
    os.system("/usr/bin/play \"|rec --buffer 2096 -d pitch -300 echos 0.8 0.88 100 0.6 150 .5 band 1.2k 1.5k\"")

def main():
    #voiceChangerThread = threading.Thread(target = runVoiceChanger)
    #voiceChangerThread.start()
    audioMonitorThread = threading.Thread(target = runAudioMonitor)
    audioMonitorThread.start()

main()
