# install.py
# Version: 1.0.0
# Contains main processing code required for DaftPunk cosplay
# Author: Billy Wood

import os
import animationPlayer
import threading
from mouthAnims import runMouthAnims

def runVoiceChanger():
    os.system("play \"|rec --buffer 2096 -d synth sine fmod 5 band 1.2k 1.5k\"")

def main():
    voiceChangerThread = threading.Thread(target=runVoiceChanger)
    voiceChangerThread.start()
    mouthAnimsThread = threading.Thread(target = runMouthAnims)
    mouthAnimsThread.start()

main()
