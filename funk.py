import requests
import time
from api import API
from scooter import Device

delay = 5
device = Device("f0:81:4f:ae:de:d3")
device.connect()

while True:
    device.getGPS()
    r =  API.funk(device)
    if r.json()['inUse']:
        device.unlock()
    else:
        r.json()['lock']

    time.sleep(5)

device.disconnect()
