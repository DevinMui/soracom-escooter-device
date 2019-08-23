#!/usr/bin/env python

from m365py import m365py
from m365py import m365message

import gps
from time import sleep

class Device:
    def handleMessage(self, peripheral, message, value):
        print(value)
        if message.attribute == m365message.Attribute.BATTERY_PERCENT:
            self.battery = value['battery_percent']

        if message.attribute == m365message.Attribute.SPEED:
            self.speed = value['speed_kmh']

    def __init__(self, mac):
        self.session = None
        self.speed = 0
        self.battery = 0
        self.lat = 0
        self.lng = 0
        self.mac = mac
        self.session = None

        self.scooter = m365py.M365(mac, self.handleMessage)

    def connect(self):
        self.scooter.connect()
        self.lock()

        self.session = gps.gps(mode=gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    def disconnect(self):
        self.scooter.disconnect()

        self.session = None

    def connected(self):
        print('Xiaomi M365 connected')

    def disconnected(self):
        print('Xiaomi M365 disconnected')

    def getGPS(self):
        try:
            self.battery = self.scooter.request(m365message.battery_percentage)
            self.speed = self.scooter.request(m365message.speed) or 0.0
            data = self.session.next()
            if(data['class'] == 'TPV'):
                self.lat = getattr(data,'lat',0.0)
                self.lng = getattr(data,'lon',0.0)
                return 1
            else:
                self.getGPS()
                sleep(1)

        except Exception as e:
            print(e)
            return 0

    def lock(self):
        self.scooter.request(m365message.turn_on_lock)

    def unlock(self):
        self.scooter.request(m365message.turn_off_lock)
