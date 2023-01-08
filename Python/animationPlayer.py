# animationPlayer.py
# Version: 1.0.0
# Plays stored animations on an attached 8x8 LED matrix.
# Author: Billy Wood

import png
import sys
import time
from rpi_ws281x import PixelStrip

animPin = 13
ledCount = (8 * 8)
ledFreqHz = 800000   # LED signal frequency in hertz (usually 800khz)
ledDma = 10          # DMA channel to use for generating signal (try 10)
ledBrightness = 255  # Set to 0 for darkest and 255 for brightest
ledInvert = False    # True to invert the signal (when using NPN transistor level shift)
ledChannel = 1       # Is 1 for GPIO 13

ledMatrix = PixelStrip(ledCount, animPin, ledFreqHz, ledDma, ledInvert, ledBrightness, ledChannel)
ledMatrix.begin()

class PixelColourData:
    r: int
    g: int
    b: int
    a: int

def playAnimation(pathToSpriteSheet, delayBetweenFrames):
    spriteInfo = png.Reader(filename=pathToSpriteSheet).asRGBA8()
    spriteColourArray = list(spriteInfo[2])

    # Check the length of the image to see the length of the animation
    imageRowCount = len(spriteColourArray)
    imageColumnCount = len(spriteColourArray[0] / 4)
    if((imageRowCount != 8) or (imageColumnCount & 8 != 0)):
        print("Error, image has an unexpected size, should be 8 x (divisible by 8)")
        sys.exit()

    for i in range(0, imageColumnCount / 8):
        for y in range(0, 8):
            for x in range(0, 8):
                imageXPixel = (i * 8) + (x * 4)
                pixel = PixelColourData(spriteColourArray[y][imageXPixel + 0], spriteColourArray[y][imageXPixel + 1], spriteColourArray[y][imageXPixel + 2], spriteColourArray[y][imageXPixel + 3])
                if(pixel.a == 255):
                    # ignore the pixel if the alpha is set to 100%
                    pixel.r = pixel.g = pixel.b = 0
                pixelToWrite = x * y
                if(y % 2 != 0): # If the row we're looking at is odd the matrixes pixel number is reversed
                    pixelToWrite = (8 - x) * y
                ledMatrix.setPixelColorRGB(pixelToWrite, pixel.r, pixel.g, pixel.b)
        ledMatrix.show()
        time.sleep(delayBetweenFrames / 1000)

def clearMatrix():
    for y in range(0, 8):
        for x in range(0, 8):
            ledMatrix.setPixelColorRGB((y * x), 0, 0, 0)
    ledMatrix.show()
