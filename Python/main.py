# install.py
# Version: 1.0.0
# Contains main processing code required for DaftPunk cosplay
# Author: Billy Wood

import os
import animationPlayer
import threading
from mouthAnims import runMouthAnims
from audioMonitor import runAudioMonitor

def runVoiceChanger():
    os.system("play \"|rec --buffer 2096 -d synth sine fmod 5 echos 0.8 0.88 50 0.6\"")

def main():
    voiceChangerThread = threading.Thread(target=runVoiceChanger)
    voiceChangerThread.start()
    audioMonitorThread = threading.Thread(target = runAudioMonitor)
    audioMonitorThread.start()
    mouthAnimsThread = threading.Thread(target = runMouthAnims)
    mouthAnimsThread.start()

main()
