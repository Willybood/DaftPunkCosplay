# audioMonitor.py
# Version: 1.0.0
# Contains audio monitoring and relevant LED output code
# Author: Billy Wood

import time
from rpi_ws281x import PixelStrip, Color
import RPi.GPIO as GPIO

# This function is run once and contains the loop that handles the audiomonitoring
def runAudioMonitor():
    audioDetectorPin = 14
    animPin = 18
    timeBetweenLedChanges = 50 # ms
    ledCount = 7
    ledColours = [Color(255, 0, 0), Color(255, 128, 0), Color(255, 255, 0), Color(0, 255, 0), Color(0, 0, 255), Color(76, 0, 153), Color(127, 0, 255)]
    ledFreqHz = 800000   # LED signal frequency in hertz (usually 800khz)
    ledDma = 10          # DMA channel to use for generating signal (try 10)
    ledBrightness = 255  # Set to 0 for darkest and 255 for brightest
    ledInvert = False    # True to invert the signal (when using NPN transistor level shift)
    ledChannel = 0       # Is 0 for GPIO 18

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(audioDetectorPin, GPIO.IN)

    strip = PixelStrip(ledCount, animPin, ledFreqHz, ledDma, ledInvert, ledBrightness, ledChannel)
    strip.begin()

    currentActiveLed = 0
    while True:
        if(GPIO.input(audioDetectorPin)):
            if(currentActiveLed < ledCount):
                currentActiveLed = currentActiveLed + 1
        else:
            if(currentActiveLed > 0):
                currentActiveLed = currentActiveLed - 1

        for i in range (0, ledCount):
            if(i < currentActiveLed):
                strip.setPixelColor(ledCount - i, ledColours[i])
            else:
                strip.setPixelColor(ledCount - i, Color(0, 0, 0))
        strip.show()
        time.sleep(timeBetweenLedChanges / 1000.0)
