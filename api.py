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
        url = 'https://funk.soracom.io:8888'
        data = {
            'event': {
                'coords': {
                    'lng': device.lng,
                    'lat': device.lat
                },
                'battery': device.battery,
                'speed': device.speed
            }
        }
        r = requests.post(url, json=data)
        return r.json()

    '''
        This method sends our device data to SORACOM Harvest
        which we can use in conjunction with SORACOM Lagoon
        to display data in a graphical format.
    '''
    @staticmethod
    def harvest():
        url = 'https://harvest.soracom.io'
        data = {
            'lng': device.lng,
            'lat': device.lat
            'battery': device.battery,
            'speed': device.speed
        }
        r = requests.post(url, json=data)
        return r.json()
