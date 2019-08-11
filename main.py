#!/usr/bin/env python

from scooter import Device
from api import API
from time import sleep

def main():
    delayInSec = 1
    config = {
        
    }
    device = Device(config)

    prevData = device.data
    while True:
        device.getData()
        if(device.data != prevDev.data):
            res = API.funk(device)
            API.harvest(device)

            if(res['inUse']):
                scooter.turnOn()
            else:
                scooter.turnOff()

            prevData = device.data
            sleep(delayInSec)

if __name__ == '__main__':
    main()
