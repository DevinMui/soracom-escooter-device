#!/usr/bin/env python

from m365py import m365py
from m365py import m365message

import gps

class Device:
    def handleMessage(self, peripheral, message, value):
        if message.attribute == m365message.Attribute.BATTERY_PERCENT:
            self.battery = value['battery_percent']

        if message.attribute == m365message.Attribute.SPEED:
            self.speed = value['speed']

    def __init__(self, mac, config):
        self.session = None
        self.speed = 0
        self.battery = 0
        self.lat = 0
        self.lng = 0

        self.scooter = m365py.M365(mac, self.handleMessage)
        self.scooter.set_connected_callback(self.connected)
        self.scooter.set_disconnected_callback(self.disconnected)

    def connect(self):
        self.scooter.connect()

        self.session = gps.gps("localhost", "2947")
        self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    def disconnect(self):
        self.scooter.disconnect()

        self.session = None

    def connected(self):
        print('Xiaomi M365 connected')
    
    def disconnected(self):
        print('Xiaomi M365 disconnected')
    
    def getGPS(self):
        try:
            data = self.session.next()
            lng = data.lon
            lat = data.lat
            return 1
        except Exception as e:
            print(e)
            return 0

    def lock(self):
        self.scooter.request(m365message.turn_on_lock)

    def unlock(self):
        self.scooter.request(m365message.turn_off_lock)
