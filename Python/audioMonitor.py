# audioMonitor.py
# Version: 1.0.0
# Contains audio monitoring and relevant LED output code
# Author: Billy Wood

import time
from rpi_ws281x import PixelStrip, Color
import RPi.GPIO as GPIO
import math

# This function is run once and contains the loop that handles the audiomonitoring
def runAudioMonitor():
    audioDetectorPin = 25
    ledOutPin = 22
    animPin = 12
    timeBetweenGpioChecks = 1 # ms
    timeBetweenLedChanges = 100 # ms
    ledCount = 8
    ledColours = [Color(0, 0, 255), Color(0, 0, 255), Color(0, 0, 255), Color(0, 0, 255), Color(0, 0, 255), Color(0, 0, 255), Color(0, 0, 255), Color(0, 0, 255)]
    ledFreqHz = 800000   # LED signal frequency in hertz (usually 800khz)
    ledDma = 10          # DMA channel to use for generating signal (try 10)
    ledBrightness = 255  # Set to 0 for darkest and 255 for brightest
    ledInvert = False    # True to invert the signal (when using NPN transistor level shift)
    ledChannel = 0       # Is 0 for GPIO 18

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(audioDetectorPin, GPIO.IN)
    GPIO.setup(ledOutPin, GPIO.OUT)

    strip = PixelStrip(ledCount, animPin, ledFreqHz, ledDma, ledInvert, ledBrightness, ledChannel)
    strip.begin()

    signalDetected = False
    currentActiveLed = 0
    secondsAtLastLedChange = time.time()
    while True:
        currentSeconds = time.time()
        secondsSinceLastLedChange = currentSeconds - secondsAtLastLedChange
        if(not signalDetected): # Only read the GPIO if signalDetected is false, that way positive reads have priority
            signalDetected = GPIO.input(audioDetectorPin)
        if(secondsSinceLastLedChange > (timeBetweenLedChanges / 1000.0)):
            if(signalDetected):
                if(currentActiveLed < math.ceil(ledCount / 2)):
                    currentActiveLed = currentActiveLed + 1
            else:
                if(currentActiveLed > 0):
                    currentActiveLed = currentActiveLed - 1

            for i in range (0, math.ceil(ledCount / 2)):
                ledToChange1 = math.floor(ledCount / 2) + i
                ledToChange2 = (math.floor(ledCount / 2) - i) - 1
                print(str(ledToChange1) + ", " + str(ledToChange2))
                if(i < currentActiveLed):
                    strip.setPixelColor(ledToChange1, ledColours[ledToChange1])
                    strip.setPixelColor(ledToChange2, ledColours[ledToChange2])
                else:
                    strip.setPixelColor(ledToChange1, Color(0, 0, 0))
                    strip.setPixelColor(ledToChange2, Color(0, 0, 0))
            strip.show()
            secondsAtLastLedChange = currentSeconds
            GPIO.output(ledOutPin, signalDetected)
            signalDetected = False
        time.sleep(timeBetweenGpioChecks / 1000.0)
