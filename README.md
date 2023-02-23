# Daft Punk Cosplay
 A Daft Punk Cosplay created for London MCM ComicCon 2023. It consists of a set of LEDs and sound changer embedded into a helmet.
 The LED strip responds to the user talking, and the LED matrix plays animations when buttons are pushed.
 
 <div align="center"><img src="Media/helmetInAction.gif"  width="100%" height="100%"><img src="Media/helmetAnims.gif"  width="100%" height="100%"></div>
 
 This design also features an 3D printed logo design which is then stitched onto the back and has threaded EL wire contained within.
 
 <div align="center"><img src="Media/daftPunkElWire.jpg"  width="30%" height="30%"></div>
 
 ## Bill of materials
  - [Raspberry Pi Zero W](https://www.amazon.co.uk/Raspberry-Pi-Zero-Wireless-model/dp/B06XFZC3BX/ref=sr_1_3?crid=2EPJH006L9QOY&keywords=pi+zero+w&qid=1673994361&sprefix=pi+zero+w%2Caps%2C72&sr=8-3)
  - [WS2812B 8x8 LED matrix](https://www.amazon.co.uk/AZUOCN-Flexible-Individually-Addressable-Programmable/dp/B09DV8PZY1/ref=sr_1_6?crid=1KSCBGC0E4RQ8&keywords=WS2812B+led+matrix&qid=1673994347&sprefix=ws2812b+led+matrix%2Caps%2C64&sr=8-6)
  - [WS2812B LED strip, cut into 2 7 LED segments](https://www.amazon.co.uk/Individually-Addressable-Programmable-Waterproof-Decoration/dp/B0BLRN29V2/ref=sr_1_6?crid=13KDXVTPKGYKK&keywords=WS2812B+led+strip&qid=1673994295&sprefix=ws2812b+led+strip%2Caps%2C74&sr=8-6)
  - A USB sound card and adapter for the Pi
  - [A small lapel mic](https://www.amazon.co.uk/AGPTEK-Microphone-Professional-Omnidirectional-Condenser/dp/B07SHSHW6H/ref=sr_1_5?crid=2WSFKFJUFFI6U&keywords=lapel+mic&qid=1673994500&sprefix=lapel+mic%2Caps%2C72&sr=8-5)
  - [A powered wired speaker](https://www.amazon.co.uk/dp/B07PDC69KT/ref=twister_B07PJNV454?_encoding=UTF8&psc=1)
  - 5 x little breadboard buttons
  - 2 x solderable breadboards
  - [Sound detector with digital output](https://www.amazon.co.uk/gp/product/B089QHMC8Y/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)
  - 6 x 1.5 metre wires
  - 9 x 1.0 metre wires
  - 3 x 0.3 metre wires
  - A set of [Dupont cables](https://www.amazon.co.uk/gp/product/B07SYKPB86/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
  - A set of breadboard jumpers
  - One black suit, shirt, and tie
  - [A spaceman helmet](https://www.amazon.co.uk/gp/product/B01HQTGPIS/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
  - Modelling cardboard for the glove parts
  - Some black primer, gold, and clear finisher spraypaint to apply to the helmet and glove parts.
  - Natural 3D printer PLA
  - [Neon EL wire](https://www.amazon.co.uk/gp/product/B099FNFCY7/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
  - Some long thin black gloves
 ## Installation
On the Pi you can install the script by cloning the repository and running the command:
```
sudo python3 ./Install/install.py
```
The construction of the electronics can be seen in the Fritzing diagram:

![alt text](https://github.com/Willybood/DaftPunkCosplay/blob/main/Fritzing/Head%20electronics_bb.png)

The lapel mic and sound detector were placed on the USB matrix in front of the mouth.
The gloves were made by cutting the modelling cardboard using a laser cutter and [the input SVG file](https://github.com/Willybood/DaftPunkCosplay/blob/main/Laser%20cuts/glove.svg).
The logo on the back was made using [this laser cut design](https://www.thingiverse.com/thing:683140) from Thingiverse (with special thanks to [Andyways](https://www.thingiverse.com/andyways)). It's available in the repo [here](https://github.com/Willybood/DaftPunkCosplay/blob/main/3D%20prints/DaftP_logo_mk1.1.stl) if needed.
## Running
Browse to the repo's folder and run the below command:
```
sudo python3 ./Python/main.py
```
