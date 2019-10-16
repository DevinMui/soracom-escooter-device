import requests
import time
from api import API
from scooter import Device

delay = 5
mac = "f0:81:4f:ae:de:d3"
device = Device(mac)
device.connect()

while True:
    device.getGPS()
    r =  API.funk(device)
    if r.json()['body']['inUse']:
        device.unlock()
    else:
        device.lock()

    time.sleep(5)

device.disconnect()
