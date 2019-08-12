#!/usr/bin/env python

from scooter import Device
from api import API
from time import sleep

def main():
    delayInSec = 1
    config = {
        
    }
    device = Device(config)
    device.connect()

    prevDevice = device
    while True:
        if not device.getGPS():
            continue

        if (device.speed != prevDevice.speed or
            device.battery != prevDevice.battery or
            device.lat != prevDevice.lat or
            device.lng != prevDevice.lng):
            
            res = API.funk(device)
            API.harvest(device)

            if(res['inUse']):
                device.unlock()
            else:
                device.lock()

            prevDevice = device
            sleep(delayInSec)

    device.disconnect()

if __name__ == '__main__':
    main()
