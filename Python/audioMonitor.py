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
    ledOutPin = 23
    animPin = 12
    timeBetweenGpioChecks = 1 # ms
    timeBetweenLedChanges = 100 # ms
    ledCount = 8
    ledColours = [Color(0, 255, 0), Color(0, 255, 0), Color(0, 255, 0), Color(0, 255, 0), Color(0, 255, 0), Color(0, 255, 0), Color(0, 255, 0), Color(0, 255, 0)]
    ledFreqHz = 800000   # LED signal frequency in hertz (usually 800khz)
    ledDma = 10          # DMA channel to use for generating signal (try 10)
    ledBrightness = 255  # Set to 0 for darkest and 255 for brightest
    ledInvert = False    # True to invert the signal (when using NPN transistor level shift)
    ledChannel = 0       # Is 0 for GPIO 18

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(audioDetectorPin, GPIO.IN)
    GPIO.setup(ledOutPin, GPIO.OUT)
    pi_pwm = GPIO.PWM(ledOutPin, 1000)
    pi_pwm.start(0)

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
        if(secondsSinceLastLedChange > ((timeBetweenLedChanges / 2) / 1000.0)):
            if(signalDetected):
                if(currentActiveLed < ledCount):
                    currentActiveLed = currentActiveLed + 1
            else:
                if(currentActiveLed > 0):
                    currentActiveLed = currentActiveLed - 1

            for i in range (0, math.ceil(ledCount / 2)):
                ledToChange1 = math.floor(ledCount / 2) + i
                ledToChange2 = (math.floor(ledCount / 2) - i) - 1
                if(i < currentActiveLed / 2):
                    strip.setPixelColor(ledToChange1, ledColours[ledToChange1])
                    strip.setPixelColor(ledToChange2, ledColours[ledToChange2])
                else:
                    strip.setPixelColor(ledToChange1, Color(0, 0, 0))
                    strip.setPixelColor(ledToChange2, Color(0, 0, 0))
            strip.show()
            secondsAtLastLedChange = currentSeconds
            pi_pwm.ChangeDutyCycle((currentActiveLed / ledCount) * 100)
            signalDetected = False
        time.sleep(timeBetweenGpioChecks / 1000.0)
