#!/usr/bin/env python

import requests

class API:

    '''
        This method sends our device data to SORACOM Funk
        which forwards our data to AWS Lambda in a secure
        manner.
    '''
    @staticmethod
    def funk(device):
        url = 'http://funk.soracom.io'
        data = {
            'mac': device.mac,
            'coords': {
                'lng': device.lng,
                'lat': device.lat
            },
            'battery': device.battery,
            'speed': device.speed
        }
        r = requests.post(url, json=data)
        return r

    '''
        This method sends our device data to SORACOM Harvest
        which we can use in conjunction with SORACOM Lagoon
        to display data in a graphical format.
    '''
    @staticmethod
    def harvest(device):
        url = 'http://harvest.soracom.io'
        data = {
            'mac': device.mac,
            'lng': device.lng,
            'lat': device.lat,
            'battery': device.battery,
            'speed': device.speed
        }
        r = requests.post(url, json=data, timeout=15)
        return r
