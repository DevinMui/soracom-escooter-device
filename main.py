#!/usr/bin/env python

from scooter import Device
from api import API
from time import sleep
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description='Control Xiaomi M365 and talk to SORACOM and AWS Lambda')
    parser.add_argument('-m', '--mac', type=str, required=True, help='Xiaomi M365 bluetooth MAC address') 
    args = parser.parse_args()

    delayInSec = 5

    device = Device(args.mac)
    device.connect()

    prevDevice = device
    while True:
        if not device.getGPS():
            continue

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
