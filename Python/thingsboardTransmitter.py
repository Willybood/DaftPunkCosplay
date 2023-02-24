# thingsboardTransmitter.py
# Version: 1.0.0
# Transmits data to the relevant Thingsboard
# Author: Billy Wood

import paho.mqtt.client as mqtt
import json

thingsboardHost = 'thingsboard.cloud'
accessToken = 'K9ZrUvPByvB4FYVChHUl'
keepAliveInterval = 30 # seconds

class ThingsBoardTransmitter:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.username_pw_set(accessToken)
        self.client.connect(thingsboardHost, 1883, keepAliveInterval)
        self.client.loop_start()

    def transmit(self, key, value):
        data = {key: value}
        self.client.publish('v1/devices/me/telemetry', json.dumps(data))
