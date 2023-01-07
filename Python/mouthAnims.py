# mouthAnims.py
# Version: 1.0.0
# Contains mouth animation and relevant GPIO code
# Author: Billy Wood

import RPi.GPIO as GPIO

# This function is run once and contains the loop that handles the mouth animations
def runMouthAnims():
    button1 = 2
    button2 = 3
    button3 = 4
    button4 = 17
    button5 = 27
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        if(not GPIO.input(button1)):
            print("Button 1 pushed")
        if(not GPIO.input(button2)):
            print("Button 2 pushed")
        if(not GPIO.input(button3)):
            print("Button 3 pushed")
        if(not GPIO.input(button4)):
            print("Button 4 pushed")
        if(not GPIO.input(button5)):
            print("Button 5 pushed")
