# mouthAnims.py
# Version: 1.0.0
# Contains mouth animation and relevant GPIO code
# Author: Billy Wood

import RPi.GPIO as GPIO
from animationPlayer import playAnimation, clearMatrix
import time

timeBetweenGpioChecks = 1 # ms
thingsboardAnimKey = "Played Animation"

# This function is run once and contains the loop that handles the mouth animations
def runMouthAnims(thingsBoardTransmitter):
    button1 = 2
    button2 = 3
    button3 = 4
    button4 = 17
    button5 = 27
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button1, GPIO.IN) # Physical pull-up present on the GPIO, soft pullup not needed
    GPIO.setup(button2, GPIO.IN) # Physical pull-up present on the GPIO, soft pullup not needed
    GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    animationPlaying = False

    while True:
        if(not GPIO.input(button1)):
            if(not animationPlaying):
                animationPlaying = True
                thingsBoardTransmitter.transmit(thingsboardAnimKey, "Hello")
            playAnimation("/home/pi/DaftPunkCosplay/pixelart animations/Hello.png", 100)
        elif(not GPIO.input(button2)):
            if(not animationPlaying):
                animationPlaying = True
                thingsBoardTransmitter.transmit(thingsboardAnimKey, "Yes")
            playAnimation("/home/pi/DaftPunkCosplay/pixelart animations/Yes.png", 300)
        elif(not GPIO.input(button3)):
            if(not animationPlaying):
                animationPlaying = True
                thingsBoardTransmitter.transmit(thingsboardAnimKey, "No")
            playAnimation("/home/pi/DaftPunkCosplay/pixelart animations/No.png", 300)
        elif(not GPIO.input(button4)):
            if(not animationPlaying):
                animationPlaying = True
                thingsBoardTransmitter.transmit(thingsboardAnimKey, "Heart")
            playAnimation("/home/pi/DaftPunkCosplay/pixelart animations/Heart.png", 150)
        elif(not GPIO.input(button5)):
            if(not animationPlaying):
                animationPlaying = True
                thingsBoardTransmitter.transmit(thingsboardAnimKey, "Talk")
            playAnimation("/home/pi/DaftPunkCosplay/pixelart animations/Talk.png", 300)
        else:
            # Clear the LED matrix
            clearMatrix()
            animationPlaying = False
        time.sleep(timeBetweenGpioChecks / 1000.0)
